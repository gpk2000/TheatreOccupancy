from django.urls import path

from .views import OccupyView

urlpatterns = [
    path('occupy/', OccupyView.as_view(), name="get_ticket_name"),
]
