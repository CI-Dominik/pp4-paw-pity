from . import views
from django.urls import path

urlpatterns = [
    path('add_animal/', views.add_animal, name='add_animal'),
    path('', views.animals, name='animals'),
]