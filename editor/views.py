from django.shortcuts import render

from .serializer import ImageSerializer
from .models import Image
# from .effects import rgb_to_gray

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

def index(request):
    """The server index page"""
    return render(request, 'editor/index.html')

class ImageListView(APIView):
    """Return a list of all the images"""
    serializer_class = ImageSerializer
    
    def get(self, request, format=None):
        serializer = self.serializer_class(Image.objects.all(), many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        print("hue")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'Message': '403 Forbidden'}, status=status.HTTP_409_CONFLICT)

class ImageView(APIView):
    """Return a image"""    
    
    def get(self, request, image_id, format=None):
        image = Image.objects.get(id=image_id)
        serializer = ImageSerializer(image)
        return Response(serializer.data)
