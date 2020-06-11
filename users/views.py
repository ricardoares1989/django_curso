"""User vies"""
# Django imports
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Exceptions
# from django.db.utils import IntegrityError


# local imports
# from django.contrib.auth.models import User
from users.models import Profile


# Forms
from users.forms import ProfileForm, SignupForm

# Create your views here.


def signup(request):
    """singup view"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(
        request=request,
        template_name='users/signup.html',
        context={'form':form},
        #
    )

def update_profile(request):
    """Update user profile view"""
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            # Tenemos que redirigir a algun lugar.
            return redirect('update_profile')
    else:
        form = ProfileForm()
    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form,
        }
    )



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




