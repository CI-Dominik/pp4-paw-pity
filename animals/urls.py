from . import views
from django.urls import path

urlpatterns = [
    path('add_animal/', views.add_animal, name='add_animal'),
    path('delete_animal/<int:animal_id>', views.delete_animal,
         name='delete_animal'),
    path('edit_animal/<int:animal_id>', views.edit_animal, name='edit_animal'),
    path('', views.animals, name='animals'),
]
