
#mapping url to call view

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
