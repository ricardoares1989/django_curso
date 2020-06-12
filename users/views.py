"""User vies"""
# Django imports
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import DetailView, FormView, UpdateView
# Exceptions
# from django.db.utils import IntegrityError

#Models
from django.contrib.auth.models import User
from posts.models import Post

# local imports
# from django.contrib.auth.models import User
from users.models import Profile


# Forms
from users.forms import  SignupForm

# Create your views here.
class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view"""
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_objetct_name = 'user'
    # Solo va a usar este query base para especificar el modelo final
    def get_context_data(self, **kwargs):
        """Add user's post to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('created')
        return context

class SignupView(FormView):
    """USers signup view"""
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:log_in')
    def form_valid(self, form):
        """Save Form Data"""
        form.save()
        return super().form_valid(form)


class UpdateUserView(LoginRequiredMixin, UpdateView):
    """Update user profile views"""
    template_name = 'users/update_profile.html'
    model = Profile
    # Ya no requerimos el form.
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """ return users profile"""
        return self.request.user.profile

    def get_success_url(self):
        """Return to users profile"""
        # Como el objeto se trajo de forma diferente entonces tenemos que sobreescribir el metood.
        username = self.object.user.username
        # self.object es el profile.
        return reverse('users:detail', kwargs={'username':username})

class LoginView(auth_views.LoginView):
    """Login view"""
    template_name = 'users/login_temp.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view"""
    template_name = 'users/logged_out.html'






