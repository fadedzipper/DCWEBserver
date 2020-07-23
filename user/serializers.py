from rest_framework import serializers

from rest_framework import serializers
from user import models
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):

    date_joined = serializers.DateTimeField(format("%Y-%m-%d %H:%M:%S"),input_formats=["%Y-%m-%d %H:%M:%S", ],read_only=True)

    class Meta:
        model = models.User
        fields = ['id','name','num','username','email','phone','gender', \
                'info','last_login','is_active','date_joined','password', 'is_superuser']

        extra_kwargs = {
            'last_login':{'read_only':True,"required":False},
            'password':{'write_only':True}
        }



    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        print("OK",user.password)
        user.save()
        return user


    # def validate_password(self,value):
    #     print("ok")
    #     if len(value) < 6:
    #         raise serializers.ValidationError("密码必须大于6位")
    #     return value

    def validate(self, data):
        password = data.get('password',None)
        if password and len(password) <6:
            raise serializers.ValidationError("密码必须大于6位")

        return data


    def get_gender(self, obj):
         if obj.gender == 1 :
             return "男"

         return "女"



class UserUpdateSerializer(UserSerializer):

    gender = serializers.IntegerField()
    class Meta:
        model = models.User
        fields = ['id','name','num','username','email','phone','gender', \
                  'info','is_active', 'password']



class UserUpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'is_active']




class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):

        data = super().validate(attrs)

        user = self.user
        data['id'] = user.id
        data['username'] = user.username
        data['last_name'] = user.last_name
        data['perms'] = user.get_all_permissions()
        data['group'] = user.groups.all().values('id','name')

        return data






