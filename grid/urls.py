
from django.urls import path,re_path,include
#from .views import AddGridView,GridListView,DeleteGridView

from rest_framework.routers import SimpleRouter
from .views import GridModeViewSet
#from .import views

router = SimpleRouter()
router.register('Grid',GridModeViewSet)


urlpatterns = [
    #path('ListGrid',GridListView.as_view()),
    #path('AddGrid',AddGridView.as_view()),
    #path('DeleteGrid',DeleteGridView.as_view()),

]   + router.urls
