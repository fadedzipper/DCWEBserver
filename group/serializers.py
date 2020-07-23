from rest_framework import serializers
from django.contrib.auth.models import Group,Permission



class GroupAddSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name','permissions','user_set']
        extra_kwargs = {
            'permissions':{'required':False},
            'user_set':{'required':False}
        }


# class GroupSerialzer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['id','name','permissions','user_set']
#         depth = 1


# class GroupSerialzer(serializers.ModelSerializer):
#
#     permissions = serializers.StringRelatedField(many=True)
#     user_set = serializers.StringRelatedField(many=True)
#
#     class Meta:
#         model = Group
#         fields = ['id','name','permissions','user_set']


# class GroupSerialzer(serializers.ModelSerializer):
#
#     permissions = serializers.SlugRelatedField(many=True,slug_field='codename',queryset=Permission.objects.all())
#
#     class Meta:
#         model = Group
#         fields = ['id','name','permissions','user_set']



class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id','name']


class GroupSerialzer(serializers.ModelSerializer):

    permissions = PermissionsSerializer(many=True,read_only=True)

    class Meta:
        model = Group
        fields = ['id','name','permissions','user_set']

    # def create(self, validated_data):
    #     permissions = validated_data.pop('permissions')
    #     group = super().create(validated_data)
    #     print(permissions)
    #     pass
    #
    #     return group









