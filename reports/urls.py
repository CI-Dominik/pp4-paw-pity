from . import views
from django.urls import path

urlpatterns = [
    path('report/<int:animal_id>', views.report_details, name='report_details'),
    path('', views.reports_view, name='reports'),
]
