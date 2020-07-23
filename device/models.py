from django.db import models
from user.models import User
from grid.models import Grid
# Create your models here.



class Device(models.Model):
    # 硬件信息

    mac = models.CharField(default='',max_length=100,verbose_name="设备mac地址")
    serial = models.CharField(default='',max_length=100,verbose_name='设备序列号',unique=True)
    is_register = models.BooleanField(default=False,verbose_name="是否激活（是否由前端激活）")
    is_enable = models.BooleanField(default=False,verbose_name="可用状态（故障）")
    is_online = models.BooleanField(default=False,verbose_name="在线状态（心跳包监控在线状态）")
    register_time = models.DateTimeField(auto_now_add=True,verbose_name="设备注册时间")
    active_time = models.DateTimeField(auto_now_add=True, verbose_name="设备激活时间",null=True)
    last_login_time = models.DateTimeField(auto_now_add=True,verbose_name="设备最上线时间",null=True)
    last_logout_time = models.DateTimeField(auto_now_add=True,verbose_name="设备最后下线时间",null=True)

    # 设备描述
    name = models.CharField(default='', null=True, max_length=100, verbose_name="设备名称")
    info = models.CharField(default='', null=True, max_length=100, verbose_name="设备描述")
    x_index = models.FloatField(default=0.0, null = True)
    y_index = models.FloatField(default=0.0, null = True)
    is_bind = models.BooleanField(default=False,null=True,verbose_name="设备是否绑定到网格")
    city = models.CharField(default='', null=True, max_length=40, verbose_name="设备所在城市")
    grid = models.ForeignKey(Grid, null=True, blank=True, on_delete=models.SET_NULL)
    # ...

    def __str__(self):
        return str(self.serial)


class DeviceSecret(models.Model):
    dev_passwd = models.CharField(default='',max_length=100,verbose_name="设备秘钥")
    dev_key = models.CharField(default='',max_length=100,verbose_name="设备通信秘钥")
    device = models.OneToOneField(Device,on_delete=models.CASCADE)



class DeviceConf(models.Model):
    device_id = models.OneToOneField(Device,on_delete=models.PROTECT)
    PM25 = models.IntegerField(default=0,verbose_name="pm2.5阈值")
    PM10 = models.IntegerField(default=0,verbose_name="pm10阈值")
    SO2 = models.IntegerField(default=0)
    NO2 = models.IntegerField(default=0)
    CO = models.IntegerField(default=0)
    O3 = models.IntegerField(default=0)
    WindSpeed = models.IntegerField(default=0)
    Light = models.IntegerField(default=0)
    CO2 = models.IntegerField(default=0)
    Temperature = models.IntegerField(default=0)
    Humidity = models.IntegerField(default=0)
    AirPressure = models.FloatField(default=0)
    Frequency = models.IntegerField(default=0,verbose_name="采集平率")
    update_status = models.BooleanField(default=0,verbose_name="设备同步状态")
    update_time = models.DateTimeField(auto_now=True,verbose_name="更新时间",null=True)
    device_update_time = models.DateTimeField(auto_now=True, verbose_name="设备同步时间",null=True)



class DeviceData(models.Model):
    device = models.OneToOneField(Device,on_delete=models.PROTECT)
    PM25 = models.IntegerField(default=0)
    PM10 = models.IntegerField(default=0)
    SO2 = models.IntegerField(default=0)
    NO2 = models.IntegerField(default=0)
    CO = models.IntegerField(default=0)
    O3 = models.IntegerField(default=0)
    WindSpeed = models.IntegerField(default=0)
    WindDirection = models.CharField(default='',max_length=100)
    Light = models.IntegerField(default=0)
    CO2 = models.IntegerField(default=0)
    Temperature = models.IntegerField(default=0)
    Humidity = models.IntegerField(default=0)
    AirPressure = models.FloatField(default=0)
    time = models.DateTimeField(auto_now_add=True)


class DeviceHistoryData(models.Model):
    device = models.ForeignKey(Device,on_delete=models.PROTECT)
    PM25 = models.IntegerField(default=0)
    PM10 = models.IntegerField(default=0)
    SO2 = models.IntegerField(default=0)
    NO2 = models.IntegerField(default=0)
    CO = models.IntegerField(default=0)
    O3 = models.IntegerField(default=0)
    WindSpeed = models.IntegerField(default=0)
    WindDirection = models.CharField(default='',max_length=100)
    Light = models.IntegerField(default=0)
    CO2 = models.IntegerField(default=0)
    Temperature = models.IntegerField(default=0)
    Humidity = models.IntegerField(default=0)
    AirPressure = models.FloatField(default=0)
    time = models.DateTimeField(auto_now_add=True)


class AlarmType(models.Model):
    name = models.CharField(default="",max_length=100,verbose_name="设备报警类型")

    def __str__(self):
        return str(self.name)


class AlarmData(models.Model):

    device = models.ForeignKey(Device,on_delete=models.PROTECT)
    alarmtype =  models.ForeignKey(AlarmType,on_delete=models.PROTECT,verbose_name="报警类型")
    value = models.CharField(default="",max_length=100,verbose_name="报警值")
    time = models.DateTimeField(auto_now_add=True,verbose_name="报警时间")
    status = models.BooleanField(default=False,verbose_name="处理状态（已处理/未处理）")
    dealwith_time = models.DateTimeField(null=True,default=None,verbose_name="处理时间")
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,default=None,verbose_name="处理人")



