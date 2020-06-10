"""User vies"""
# Django imports
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Exceptions
from django.db.utils import IntegrityError


# local imports
from django.contrib.auth.models import User
from users.models import Profile
# Create your views here.

def login_view(request):
    """Login in view."""
    if request.method == 'POST':
        print('*' * 10)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Esto hara la sesion
            return redirect('feed')
        else:
            return render(request, 'users/login.html',{'error': 'Invalid username and password'})
    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """Logout user"""
    logout(request)
    return redirect('login')


def signup(request):
    """singup view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match.'})
            # Si las contraseñas no coinciden lo que haremos sera regresar el template y añadir un mensaje de error al contexto
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(requests, 'users/signup.html', {'error':'Username is already in user.' })
        
        user = User.objects.create_user(username=username, password=password)
        user.first_name= request.POST['first_name'] 
        user.last_name= request.POST['last_name'] 
        user.email= request.POST['email'] 
        user.save()
        profile = Profile(user=user)
        profile.save()
        # Si realizamos Profile.objects.create no se salva.
        return redirect('login')
    return render(request, 'users/signup.html')