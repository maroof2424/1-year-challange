# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Blog URLs
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),

    # Auth custom views
    path('signup/', views.signup, name='signup'),
]
