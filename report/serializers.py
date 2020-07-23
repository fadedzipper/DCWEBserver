from rest_framework import serializers
from report import models

class ReportUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        fields = ['id', 'handled', 'handle_content']

        extra_kwargs={
            'handled' : {'read_only' : True}
        }

    def update(self, instance, validated_data):

        object = super().update(instance, validated_data)
        object.handled = 1
        object.save()

        return object

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        fields = ['id', 'name', 'topic', 'phone', 'email', 'handled']



class ReportListallSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        fields = ['info']


class ReportAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        fields = ['id', 'name', 'topic', 'phone', 'email', 'handled', 'info']

        extra_kwargs={
            'handled' : {'read_only' : True}
        }
