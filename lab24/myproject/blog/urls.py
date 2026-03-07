from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('media/', views.media_page, name='media'),
]