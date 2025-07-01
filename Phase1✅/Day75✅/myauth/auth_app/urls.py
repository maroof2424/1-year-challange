from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_signup_view, name='login_signup'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
