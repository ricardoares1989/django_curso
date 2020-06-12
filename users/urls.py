""" User urls"""
# Django
from django.urls import path

from users import views

    # Management
app_name = 'users'
urlpatterns = [

    path(
        route='<str:username>/', 
        view=views.UserDetailView.as_view(template_name='users/detail.html'),
        name='detail'
        ),
    path(
        route='users/log_in/', 
        view=views.login_view, 
        name='log_in'),
    path(
        route='users/logout/', 
        view=views.logout_view, 
        name='logout' ),
    path(
        route='users/signup/',  
        view=views.signup, 
        name='signup'),
    path(
        route='users/me/profile/',  
        view=views.update_profile, 
        name='update_profile'), 
]

    