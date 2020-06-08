"""User admin classes."""


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import User
# BaseUserAdmin para no tenerlo con el nombre debajo que es la clase que tendremos en linea.

# Models
from users.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin"""
    # La clase puede estar vacia y funcionar.
    list_display = ('pk','user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk','user')
    list_editable = (
        'phone_number', 'website', 'picture')
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name', 
        'user__last_name',
        'phone_number'
        )
    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff')
    fieldsets = (('Profile',
                    {'fields':(('user','picture'),)
                    }),
                ('Extra info',
                    {'fields':(('website','phone_number'),
                                ('biography'),
                )}),
                ('Metadata',
                    {'fields':(('created','modified'),),
                    }))
    readonly_fields = ('created','modified','user')

class ProfileInLine(admin.StackedInline):
    """Profile in-line admin for users."""
    model = Profile
    # Este es el modelo
    can_delete = False
    # Si se puyede borrar o no
    verbose_name_plural = 'profiles'
    # El verbose en plural cuando se este nombrando.

class UserAdmin(BaseUserAdmin):
    """Adds profile admin to base user admin."""
    inlines = (ProfileInLine,)
    list_diplay =(
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )

# Entonces para registrarlo no lo haremos con un decorador, lo haremos por medio de:
# importar from django.contrib.auth.admin import User
# Esto para poder deregistrarlo y luego tenemos que registrar nuestro nuevo admin,
# si bien solo puede recibir un modelo tambien puede recibir el modelo y la clase que 
# vamos a usar.

admin.site.unregister(User)
admin.site.register(User, UserAdmin)