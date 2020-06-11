"""User forms"""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    """Sign up form"""
    username = forms.CharField(min_length=4, max_length=50)
    password = forms.CharField(max_length=70, widget= forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70, widget= forms.PasswordInput())
    first_name = forms.CharField(min_length=2,max_length=50)
    last_name = forms.CharField(min_length=2,max_length=50)
    email = forms.CharField(min_length=6, max_length=70, widget= forms.EmailInput())
    # las validaciones que se aplicaran por default seran las validaciones correspondiente de cada widget.
    # pero tenemos que confirmar el password y que el usuario no este registrado.
    def clean_username(self):
        """Username must be unique"""
        # Tenemos que hacer querys a las base de datos.
        username = self.cleaned_data['username']
        # nos dara este dato
        username_taken = User.objects.filter(username=username)
        if username_taken:
            # con raise va a subir el error hasta el html
            raise forms.ValidationError('Username is already in use.')
        return username
        # Siempre que se haga la validacion de un campo tienes que reenviar el campo, por que al hacer clean que es el ultimo metodo
        # el valor no tendra nada.
    # So tienes cambios que dependen de otros mismos, lo que haras sera con el metodo clean.
    def clean(self):
        """Verify password confirmation match"""
        data = super().clean()
        # Esta es la forma en la que se sobrescribe nuestro metodo.
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('passwords do not match')
        return data
    def save(self):
        """Create user and profile"""
        data = self.cleaned_data
        data.pop('password_confirmation')
        # Vamos a sacar de cleaned_Data nuestro password_confirmation, por que no nos servira.
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


class ProfileForm(forms.Form):
    """Profile form"""
    # solo vamos a modificar ciertos datos de l profile.
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
