from django.urls import path,include,re_path
from rest_framework import  routers
from . import  views

router = routers.SimpleRouter()
router.register('',views.UserViewset)

urlpatterns = [
    # path('t/users/',views.UserViewset.as_view({'get':'list','post':'create'}))
] + router.urls