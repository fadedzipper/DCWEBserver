from django.urls import path,include,re_path
from .views import PermissionListView

urlpatterns = [
    path('',PermissionListView.as_view()),
]