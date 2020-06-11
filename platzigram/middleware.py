"""Platzigram middleware catalog."""
# Django 
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """Profile completion middleware

    Ensure every user that is interacting with the platform
    have their picture and biography"""

    def __init__(self, get_response):
        """Middleware inizialisation"""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile #Esta es una forma de traer los OnetoOneFields de nuestros modelos
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('update_profile'), reverse('logout')]:
                # Vamos a traer una funcion de django que se llama reverse, la cual a partir de un nombre
                # Traera la url

                        return redirect('update_profile')
        response = self.get_response(request)
        return response