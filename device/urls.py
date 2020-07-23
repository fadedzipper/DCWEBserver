from django.urls import path,include,re_path
from device import views
urlpatterns = [
    path('',views.DevicePostView.as_view()),
    path('<int:pk>/conf',views.DeviceConfView.as_view()),
    path('<int:pk>/unable',views.DeviceUnableView.as_view()),
    path('<int:pk>/update',views.DeviceupdateView.as_view()),
    path('list',views.DevicelistView.as_view()),
    path('configure', views.DeviceConflistView.as_view()),
    path('realdata', views.DeviceRealdatalistView.as_view()),
    path('historydata', views.DeviceHistorydatalistView.as_view()),
    path('alarmdata', views.DeviceAlarmdatalistView.as_view()),
    path('<int:pk>/alarmhandle', views.DeviceAlarmdataupdateView.as_view()),
    path('<int:pk>/currentdata',views.GetCurrentDataView.as_view()),
    path('AQI',views.GetAQIView.as_view()),
    path('SHAQI',views.GetAllAQIView.as_view()),
    path('<int:pk>/History',views.GetHistorytDataView.as_view()),
    path('10HistoryPM25',views.GetPM25HistoryView.as_view()),
    path('10HistoryPM10',views.GetPM10HistoryView.as_view()),
    path('10HistoryTemp',views.GetTempHistoryView.as_view()),
    path('10HistoryCO2',views.GetCO2HistoryView.as_view()),

]