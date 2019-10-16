from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('create/', views.CreateForm.as_view(), name='create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
]
