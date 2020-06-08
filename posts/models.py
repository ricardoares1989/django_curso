"""Posts models."""

# Django
from django.db import models
from django.contrib.auth.models import User

# 

# Create your models here.

class Post(models.Model):
    """Post model."""
    
    # Tenemos que relacionarlo a nuestro usuario de alguna manera.
    # Foreign Key reflejara una relacion.
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    # Una forma de importar nuestro modelo de Profile, es colocando un string, donde coloques
    # nombre de la app y luego el nombre del modelo.

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')
    # todos los charfield lo que realizan es guardar en un upload_to
    # este especifica la carpeta donde se estara guardando
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the title and username"""
        return f'{self.title} by @{self.user.username}'
