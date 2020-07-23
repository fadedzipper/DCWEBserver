from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from grid import models

from .models import Grid

import datetime
import random
#from utils.sendData import updateConfigCmd,activeCmd
from rest_framework.exceptions import APIException






#网格的序列化器
class GridSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Grid
        fields = ['id','name','location','leader','telephone']
        extra_kwargs = {
            'name':{"required":True},
            'location':{"required":True},
            'leader': {"required": True},
            'telephone': {"required": True},
        }



'''
class AddGridSerizalizer(ModelSerializer):
    class Meta:
        model = Grid
        fields = '__all__'
'''