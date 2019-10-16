from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateForm.as_view()),
    path('detail/<int:pk>/', views.PostDetailView.as_view()),
]
