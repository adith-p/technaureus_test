from django.urls import path

from . import views

app_name = 'user_auth'

urlpatterns = [
    path('',views.login_user,name='login_user'),
    path('logout/',views.logout_user,name='logout_user'),
    
]