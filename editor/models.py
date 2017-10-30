from django.db import models

class Image(models.Model):
    """Representa a imagem que será manipulada nas requisições POST e GET"""
    default_url = 'images/none/no_image.png'
    image = models.ImageField(upload_to='images/', default=default_url)
    
    def __str__(self):
        return str(self.image)

class Effect(models.Model):
    """Representa um efeito a ser aplicado na imagem"""
    default_url = 'previews/none/no_preview.png'
    preview = models.ImageField(upload_to='previews/', default=default_url)
    title = models.TextField()
    description = models.TextField()
    
    def __str__(self):
        return self.title
