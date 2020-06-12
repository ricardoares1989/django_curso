""" User urls"""
# Django
from django.urls import path

from users import views

    # Management
app_name = 'users'
urlpatterns = [


    path(
        route='users/log_in/', 
        view=views.LoginView.as_view(), 
        name='log_in'),
    path(
        route='users/logout/', 
        view=views.LogoutView.as_view(), 
        name='logout' ),
    path(
        route='users/signup/',  
        view=views.SignupView.as_view(), 
        name='signup'),
    path(
        route='users/me/profile/',  
        view=views.UpdateUserView.as_view(), 
        name='update_profile'), 
    path(
        route='<str:username>/', 
        view=views.UserDetailView.as_view(template_name='users/detail.html'),
        name='detail'
        ),
]

    