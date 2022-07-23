from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegisterAPIView.as_view(), name="register"),
    path('login/', views.UserLoginAPIView.as_view(), name="login"),
    path('logout/', views.UserLogoutAPIView.as_view(), name="logout"),
    path('users/', views.AuthUserListAPIView.as_view(), name="users"),
    path('users/<int:pk>/', views.AuthUserDetailAPIView.as_view(), name="user"),
]
