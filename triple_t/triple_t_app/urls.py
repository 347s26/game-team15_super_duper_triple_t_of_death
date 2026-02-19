from django.urls import path
from . import views
from .api import create_game

urlpatterns = [
    path('', views.index, name='index')
]
