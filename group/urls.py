from django.urls import path,include,re_path
from group.views import GroupListView

urlpatterns = [
    path('',GroupListView.as_view())
]