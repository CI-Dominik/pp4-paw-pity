from . import views
from django.urls import path

urlpatterns = [
    path('<int:animal_id>/', views.animal_detail, name='animal_detail'),
    path('<int:animal_id>/comments/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('<int:animal_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('', views.reports_view, name='reports'),
]
