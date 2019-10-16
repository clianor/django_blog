from django.urls import path

from . import views

app_name = 'auth'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('withdrawal/', views.WithdrawalView.as_view(), name='withdrawal'),
    path('logout/', views.logout_view, name='logout'),
]
