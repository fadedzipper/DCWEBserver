from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import SysLog
from .serializers import LogSerializer
from rest_framework.pagination import  PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from permission.permissions import ModelPermission
from rest_framework import permissions


# Create your views here.


class SelfPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class SyslogView(ModelViewSet):
    serializer_class = LogSerializer
    permission_classes = (permissions.IsAuthenticated, ModelPermission, )
    pagination_class = SelfPagination
    queryset = SysLog.objects.all().order_by("log_id")
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ('log_type','log_content','log_user','log_dotype')