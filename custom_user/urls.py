from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('user_login/', views.login_user, name='user_login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_user, name='logout'),
]