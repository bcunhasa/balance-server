from django.shortcuts import render
from django.conf import settings

from .serializer import ImageSerializer, GallerySerializer
from .models import Image, Gallery

from .effects import effects
from .effects import filters
from .effects import transformations

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.renderers import JSONRenderer

import json
import base64
import cv2 as cv
import numpy as np

# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

def index(request):
    """The server index page"""
    return render(request, 'editor/index.html')


class GalleryView(APIView):
    """Post requisition to get the final image"""
    serializer_class = GallerySerializer
    
    def get(self, request):
        queryset = Gallery.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response({"erro": "O JSON não é válido"}, status=status.HTTP_409_CONFLICT)


class ImageResultView(APIView):
    """Post requisition to get the final image"""
    
    def post(self, request):
        response = apply_effect(request.data['image'], request.data['effect'])
        #serializer = ImageSerializer(response)
        return Response(response)


class ImageCreateView(APIView):
    """Post requisition for a new image"""
    
    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        
        if serializer.is_valid():
            response = effects_list(base64_image=request.data['image'])
            return Response(response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def apply_effect(base64_image, effect):
    """Do the configuration to apply the effect to the image"""
    image = base64_to_img(base64_image)
    
    if effect == 'Tons de cinza':
        image = effects.grayscale(image)
    elif effect == 'Correção de iluminação':
        image = filters.light_corrector(image)
    elif effect == 'Rotação':
        image = transformations.rotation(image)
    
    effect_dict = {}
    effect_dict['image'] = img_to_base64(image)
    
    return json.dumps(effect_dict)

def effects_list(base64_image):
    """Create a list of effects"""
    image = base64_to_img(base64_image)
    effects_dict = {}
    
    effects_dict['grayscale'] = {}
    effects_dict['grayscale']['title'] = 'Tons de cinza'
    effects_dict['grayscale']['description'] = 'Transforma a imagem em uma com tons de cinza'
    effects_dict['grayscale']['preview'] = img_to_base64(effects.grayscale(image))
    
    effects_dict['light_corrector'] = {}
    effects_dict['light_corrector']['title'] = 'Correção de iluminação'
    effects_dict['light_corrector']['description'] = 'Corrige a iluminação da fotografia'
    effects_dict['light_corrector']['preview'] = img_to_base64(filters.light_corrector(image))
    
    effects_dict['rotation'] = {}
    effects_dict['rotation']['title'] = 'Rotação'
    effects_dict['rotation']['description'] = 'Rotaciona a imagem'
    effects_dict['rotation']['preview'] = img_to_base64(transformations.rotation(image))
    
    return json.dumps(effects_dict)

def base64_to_img(base64_image):
    """Converte a base64 image to a openCV image"""
    encoded_image = base64_image.split(',')[1]
    string_image = base64.b64decode(encoded_image)
    np_image = np.fromstring(string_image, dtype=np.uint8)
    image = cv.imdecode(np_image, cv.IMREAD_COLOR)
    return image

def img_to_base64(image):
    """Convete a openCV image to a base64 image"""
    image = cv.imencode('.png', image)[1].tostring()
    base64_image = base64.b64encode(image)
    base64_image = "data:image/png;base64," + base64_image.decode("utf-8")
    return base64_image
