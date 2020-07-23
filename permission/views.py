from django.shortcuts import render
from rest_framework import generics
from permission.serializers import PermissionSerializer
from django.contrib.auth.models import Permission
# Create your views here.

class PermissionListView(generics.ListAPIView):
    '''
    权限列表
    '''
    serializer_class = PermissionSerializer
    queryset = Permission.objects.exclude(name__startswith="Can")
    pagination_class = None
