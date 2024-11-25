from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

urlpatterns = [
    path('register_user/', views.register_user, name="register_user"),
    path('login_user/', views.login_user, name="login_user"),
    path('user_profile/', views.user_profile, name="user_profile"),
     path('logout_user/', views.logout_user, name='logout_user'),
    # path('register/', views.register_user, name='register'),
    # path('user_login/', views.login_user, name='user_login'),
    # path('profile/', views.profile_view, name='profile'),
    # path('logout/', views.logout_user, name='logout'),
]