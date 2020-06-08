"""Posts models."""

from django.db import models

# Create your models here.


class User(models.Model):
    """User model"""
    email= models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)
    city = models.TextField(max_length = 100, default='Null')
    country = models.TextField(max_length = 100, default='Null') 
    birthdate = models.DateField(blank=True, null=True)
    # PAra birthdate este es el valor por defecto. 
    created = models.DateTimeField(auto_now_add=True)
    # En cuanto se cree una instancia le va a cargar la fecha en la que se creo
    modified = models.DateTimeField(auto_now=True)
    # Va a añadir la fecha en la que se edito por ultima vez.
    def __str__(self):
        """Return email"""
        return self.email


