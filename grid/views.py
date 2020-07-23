from django.shortcuts import render

from django.http import JsonResponse
from django.views import View
from .models import Grid
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
from rest_framework import permissions
from permission.permissions import ModelPermission

from .serializers import GridSerizalizer

#全家桶
from rest_framework.viewsets import ModelViewSet

#分页类
from rest_framework.pagination import PageNumberPagination

#过滤器
from django_filters.rest_framework import DjangoFilterBackend

#导入状态码
from rest_framework import status

from rest_framework import generics,viewsets,filters
from django.shortcuts import get_object_or_404


from log.utils import  addlog
# Create your views here.

'''
#查看网格
class GridView(View):
    def post(self,request):
        return JsonResponse()

    def get(self,request):
        grids = Grid.objects.all()
        return JsonResponse(Grid)

class GridListView(ListAPIView):
    serializer_class = GridSerizalizer
    queryset = Grid.objects.all()


#新增网格
class AddGridView(APIView):
    def post (self,request):
        serizalizer = AddGridSerizalizer(data=request.data)
        if serizalizer.is_valid():
            serizalizer.save()
            return Response(data={"msg":"添加成功"}, status=status.HTTP_201_CREATED)
        return Response(data = serizalizer.errors,status = status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        grid = Grid.objects.all()
        serizalizer = GridSerizalizer(grid,many=True)
        return Response(serizalizer.data,status=status.HTTP_200_OK)

class AddGridView(CreateAPIView):
    serializer_class = AddGridSerizalizer
    queryset = Grid.objects.all()

#删除网格
class DeleteGridView(DestroyAPIView):
    serializer_class = GridSerizalizer
    queryset = Grid.objects.all()
'''

class MyPagination(PageNumberPagination):

    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100



#全家桶
class GridModeViewSet(viewsets.ModelViewSet):
    serializer_class = GridSerizalizer
    permission_classes = (permissions.IsAuthenticated, ModelPermission, )
    pagination_class = MyPagination
    queryset = Grid.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ('id','name','location','leader','telephone')
    #模糊查询
    search_fields = ('name','location','leader','telephone')


    def create(self, request, *args, **kwargs):
        """
        新增网格

        #### 参数说明
        | 字段名称 | 描述 | 必须 | 类型 |
        | -- | -- | -- | -- |
        | name | 网格名 | True | str |
        | location | 所在地 | True | str|
        | leader | 负责人 | True | str |
        | telephone | 联系方式 | True | int |

        """
        addlog(self.request, "网格管理", "新建网格", "POST")
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
            修改网格信息

            #### 参数说明
            | 字段名称 | 描述 | 必须 | 类型 |
            | -- | -- | -- | -- |
            | name | 网格名 | True | str |
            | location | 所在地 | True | str|
            | leader | 负责人 | True | str |
            | telephone | 联系方式 | True | int |
            """
        addlog(self.request, "网格管理", "修改网格", "PUT")
        return super().update(request, *args, **kwargs)






