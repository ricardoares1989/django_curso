"""User vies"""
# Django imports
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

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
