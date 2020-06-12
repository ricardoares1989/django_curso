"""Posts views"""

# Django
# from django.shortcuts import render, redirect
# Ya no usamos ni render ni redirect.

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy


# from django.http import HttpResponse

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post


# Create your views here.

class PostsFeedView(LoginRequiredMixin, ListView):
    """ Retunr all published posts."""
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'posts'
    # El nombre del query en el contexto queremos que sea post.

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return the post detail"""
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post"""
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')
    def get_context_data(self, **kwargs):
        """Ad user and profile to xontext."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context


