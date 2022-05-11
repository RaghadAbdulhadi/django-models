from django.urls import path
from .views import SnackListView
urlpatterns = [
    path('snack-list', SnackListView.as_view(), name='snack_list'),
]