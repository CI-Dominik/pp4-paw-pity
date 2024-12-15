from django.urls import path
from .views import complain_comment
from .views import ViewComplaintsView

urlpatterns = [
    path('complain_comment/<int:comment_id>/', complain_comment, name='complain_comment'),
    path('view_complaints/', ViewComplaintsView.as_view(), name='view_complaints'),
]