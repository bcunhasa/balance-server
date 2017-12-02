from django.db import models

class Image(models.Model):
    """Representa a imagem que será manipulada nas requisições POST e GET"""
    default_url = 'images/none/no_image.png'
    image = models.ImageField(upload_to='images/', default=default_url)
    
    def __str__(self):
        return str(self.image)

class Gallery(models.Model):
    """Representa o item de galeria que será manipulado nas requisições POST e GET"""
    uri = models.CharField(max_length=200)
    effect = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.uri)
