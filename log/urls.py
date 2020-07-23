from django.urls import path,include,re_path
from .views import SyslogView
from rest_framework.routers import  SimpleRouter



router = SimpleRouter()
router.register('logs',SyslogView)


urlpatterns = [
   ] + router.urls
