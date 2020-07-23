from rest_framework import viewsets
from . import serializers, models
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import FilterSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import TokenObtainPairView
from log.utils import  addlog


class MyPagination(PageNumberPagination):

    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100



class ReportViewSet(viewsets.ModelViewSet):

    pagination_class = MyPagination
    # serializer_class = serializers.ReportSerializer
    queryset = models.Report.objects.all().order_by('id')
    # filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    # filterset_fields = ('gender', 'is_active')
    # search_fields = ('username', 'info')
    # filter_class = UserFilterSet


    def get_serializer_class(self):
        if self.action == 'retrieve':
            addlog(self.request,"举报模块","查看举报","GET")
            return serializers.ReportListallSerializer

        if self.action == 'create':
            addlog(self.request, "举报模块", "添加举报", "POST")
            return serializers.ReportAddSerializer

        if self.action == 'update':
            addlog(self.request, "举报模块", "修改举报", "PUT")
            return serializers.ReportUpdateSerializer

        return serializers.ReportSerializer


    def list(self, request, *args, **kwargs):
        """
        获得用户列表 
        
        #### 参数说明
        | 字段名称 | 描述 | 必须 | 类型 |
        | -- | --  | -- | -- |
        | username | 用户名 | True | str |
        | password | 密码 | True | str |
        | last_name | 昵称 | True | str|
        | email | 邮箱 | True | str |
        | tel | 电话 | True | str |
        | num | 工号 | True | str |
        | gender | 性别(1男 2女) | True | int |
        | info | 备注信息 | False | int |
        | is_active | 账户状态(1 冻结 2 激活）| False |int|


        #### 响应消息：
        | Http响应码 | 原因 | 响应模型 |
        | -- | -- | -- |
        | 200 | 获取列表成功 | 返回数据 |
        | 400 | 参数格式错误 | 参数格式错误 |
        | 500 | 请求失败 | 服务器内部错误 |
        | 404 | 页面没有找到 | 页面没有找到 |
        """
        addlog(self.request, "举报模块", "查看举报用户", "GET")
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        新增用户

        #### 参数说明
        | 字段名称 | 描述 | 必须 | 类型 |
        | -- | --  | -- | -- |
        | username | 用户名 | True | str |
        | password | 密码 | True | str |
        | last_name | 昵称 | True | str|
        | email | 邮箱 | True | str |
        | tel | 电话 | True | str |
        | num | 工号 | True | str |
        | gender | 性别(1男 2女) | True | int |
        | info | 备注信息 | False | int |
        | is_active | 账户状态(1 冻结 2 激活）| False |int|


        #### 响应消息：
        | Http响应码 | 原因 | 响应模型 |
        | -- | -- | -- |
        | 201 | 添加成功 | 返回数据 |
        | 400 | 参数格式错误 | 参数格式错误 |
        | 500 | 请求失败 | 服务器内部错误 |
        | 404 | 页面没有找到 | 页面没有找到 |
        """
        addlog(self.request, "举报模块", "新增举报用户", "POST")
        return super().create(request, *args, **kwargs)



    def destroy(self, request, *args, **kwargs):

        """
        冻结用户

        #### 参数说明
        | 字段名称 | 描述 | 必须 | 类型 |
        | -- | --  | -- | -- |
        | 用户id | 被冻结用户的id  | True | int |


        #### 响应消息：
        | Http响应码 | 原因 | 响应模型 |
        | -- | -- | -- |
        | 200 | 冻结成功 | 返回数据 |
        """
        # 获取对象
        # 修改属性
        # 保存

        # id = self.kwargs.get('id')
        # try:
        #     user = models.User.objects.get(id=id)
        # except Exception as e :
        #     print(e)
        #     return Response({'msg':"找不多对象","code":404},status=status.HTTP_404_NOT_FOUND)

        report = self.get_object()
        report.handled = 1
        report.save()
        addlog(self.request, "举报模块", "冻结举报用户", "DELETE")
        return  Response({'msg':"处理成功","code":200},status=status.HTTP_200_OK)


    def retrieve(self, request, *args, **kwargs):
        '''
       
        '''
        return super().retrieve(request, *args, **kwargs)

