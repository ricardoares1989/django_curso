"""User vies"""
# Django imports
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import DetailView
# Exceptions
# from django.db.utils import IntegrityError

#Models
from django.contrib.auth.models import User
from posts.models import Post

# local imports
# from django.contrib.auth.models import User
# from users.models import Profile


# Forms
from users.forms import ProfileForm, SignupForm

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



def signup(request):
    """singup view"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:log_in')
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
            url = reverse('users:detail', kwargs={'username':request.user.username})
            # Tenemos que redirigir a algun lugar.
            return redirect(url)
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

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            
            # Esto hara la sesion
            return redirect('posts:feed')
        else:
           
            return render(request, 'users/login_temp.html' ,{'error': 'Invalid username and password'})
    # import pdb; pdb.set_trace()
    return render(request, 'users/login_temp.html')


@login_required
def logout_view(request):
    """Logout user"""
    logout(request)
    return redirect('users:log_in')




