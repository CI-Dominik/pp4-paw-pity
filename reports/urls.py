from . import views
from django.urls import path

urlpatterns = [
    path('<int:animal_id>/', views.animal_detail, name='animal_detail'),
    path('', views.reports_view, name='reports'),
]
