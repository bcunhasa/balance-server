from django.db import models

class Image(models.Model):
    """Representa a imagem que será manipulada nas requisições POST e GET"""
    image = models.ImageField(upload_to='images/', default='images/none/null_img.png')
    
    def __str__(self):
        return str(self.id)
