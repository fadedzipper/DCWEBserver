from rest_framework import serializers
from log.models import SysLog


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysLog
        fields = '__all__'


