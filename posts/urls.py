"""Posts urls."""
# Django
from django.urls import path

# Views
from posts import views

    # Vamos a colcoar nuestros argumentos posicionales.
urlpatterns = [
    path(
        route = '', 
        view= views.PostsFeedView.as_view(), 
        name='feed', 
        ),

    path(
        route = 'posts/new/', 
        view= views.CreatePostView.as_view(), 
        name='create'),
    path(
        route = 'posts/<int:pk>/',
        view = views.PostDetailView.as_view(),
        name='detail'
    ),
]