# django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """Profile model.

    Proxy model than extends the base data with other 
    information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    # Django no guarda el archivo en la base de datos, solo tiene la referencia a la base de datos.

    picture = models.ImageField(
        upload_to='users/pictures', 
        blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return Username"""
        return self.user.username
        