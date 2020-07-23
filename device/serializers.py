from rest_framework import serializers
from device import models
import datetime
import random
from utils.sendData import updateConfigCmd,activeCmd
from rest_framework.exceptions import APIException


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'


class CreateDeviceSerialzer(serializers.ModelSerializer):

    dev_passwd = serializers.CharField(write_only=True)
    serial = serializers.CharField()
    mac = serializers.CharField()

    class Meta:
        model = models.Device
        fields = ['mac','serial','dev_passwd',
                  'name','info','x_index','y_index',
                  'is_enable','is_online','is_register', 'city'] # ...

        extra_kwargs = {
            'is_enable':{'read_only':True,'required':False},
            'is_online':{'read_only':True,'required':False},
            'is_register': {'read_only': True, 'required': False}
        }



    def validate(self, attrs):

        serial = attrs.pop('serial')
        dev_passwd = attrs.pop('dev_passwd')

        try:
            device = models.Device.objects.get(serial = serial)
        except:
            raise serializers.ValidationError('设备不存在')

        if device.is_register == True:
            raise serializers.ValidationError('设备已激活')

        if dev_passwd != device.devicesecret.dev_passwd:
            raise serializers.ValidationError('设备秘钥错误')

        attrs['device'] = device

        return attrs

    def create(self, validated_data):

        device= validated_data.pop('device')
        device.name = validated_data.get('name',"")
        device.info = validated_data.get('info', "")
        device.x_index = validated_data.get('x_index', "")
        device.y_index = validated_data.get('y_index', "")
        device.is_register = True
        device.active_time = datetime.datetime.now()
        device.devicesecret.dev_key = "".join(random.sample('zyxwvutsrqponmlkjihgfedcba',11))


        # 如果当前采集服务器还没有写好，，我们只测试后端功能的话，，可以先把下面两行发送命令注释掉
        if activeCmd(device.serial,device.devicesecret.dev_key):
            raise ServiceUnavailable("发送异常")

        device.devicesecret.save()
        device.save()

        return device


class  DeviceConfSerialzer(serializers.ModelSerializer):

    class Meta:

        model = models.DeviceConf
        fields = '__all__'
        read_only_fields = ['device_id','update_status','update_time','device_update_time']

    def update(self, instance, validated_data):

        object = super().update(instance,validated_data)
        object.update_status = False
        object.update_time = datetime.datetime.now()

        key = object.device_id.devicesecret.dev_key
        serial = object.device_id.serial

        # 如果当前采集服务器还没有写好，，我们只测试后端功能的话，，可以先把下面两行发送命令注释掉
        if updateConfigCmd(serial,key):
            raise ServiceUnavailable("发送异常")

        object.save()
        return  object


class   DeviceSerializer(serializers.ModelSerializer):

    grid = serializers.StringRelatedField(many=False)

    class Meta:
        model = models.Device
        fields = ['id', 'serial', 'name', 'is_register', 'is_online', 'is_bind', 'is_enable', 'id','mac', 'x_index', 'y_index', 'info', 'grid', 'register_time', 'active_time', 'last_login_time', 'last_logout_time', 'grid', 'city']




class DeviceUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Device
        fields = ['id', 'name', 'x_index', 'y_index', 'info', 'is_enable', 'is_bind', 'grid', 'city']

    # def update(self, instance, validated_data):
    #     if object.is_bind == 1:
    #         object = super().update(instance, validated_data)
    #         object.save()
    #
    #     else:
    #         object.is_bind = 0
    #         object.save()
    #
    #     return object


class Device_unableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Device
        fields = ['id', 'is_enable']
        read_only_fields = ['is_enable']
    def update(self, instance, validated_data):
        object = super().update(instance, validated_data)
        object.is_enable = False
        object.save()
        return object


class DeviceconflistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeviceConf
        fields = '__all__'


class DevicealarmlistSerializer(serializers.ModelSerializer):

    device = serializers.StringRelatedField()
    alarmtype = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = models.AlarmData
        fields = ['id', 'device', 'alarmtype', 'value', 'time', 'status', 'dealwith_time', 'user']

class DevicealarmupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AlarmData
        fields = ['id', 'status', 'dealwith_time']
        read_only_fields = ['status']
    def update(self, instance, validated_data):
        object = super().update(instance, validated_data)
        object.status = True
        object.dealwith_time = datetime.datetime.now()
        object.save()
        return object


class DevicerealdatalistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeviceData
        fields = '__all__'

class DevicehistorydatalistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeviceHistoryData
        fields = '__all__'

# 高艺的序列化器
class DeviceHistoryDataSerialzer(serializers.Serializer):

    datafield = serializers.CharField(max_length=10)
    start_time = serializers.DateTimeField(input_formats=["%Y-%m-%d %H:%M:%S", ], required=False)
    end_time = serializers.DateTimeField(input_formats=["%Y-%m-%d %H:%M:%S", ], required=False)
