from django.urls import path
from .views import complain_comment
from .views import remove_comment, delete_complaint, view_complaints

urlpatterns = [
  path('complain_comment/<int:comment_id>/', complain_comment, name='complain_comment'),
  path('view_complaints/', view_complaints, name='view_complaints'),
  path('remove_comment/<int:comment_id>/', remove_comment, name='remove_comment'),
  path('delete_complaint/<int:complaint_id>/', delete_complaint, name='delete_complaint'),
]