
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from platzigram import views as local_views
# from posts import views as posts_views
# from users import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # include recibe dos parametros el primero es una tupla donde dice donde esta el modulo y de donde viene.
    # Despues el namespace 
    path('', include(('posts.urls', 'posts'), namespace = 'posts')),
    path('', include(('users.urls', 'users'), namespace = 'users')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


