from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListCreateTodoAPIView.as_view(), name="todos"),
    path('<int:pk>/', views.RetrieveUpdateDestroyTodoAPIView.as_view(), name="detail-todo"),
]
