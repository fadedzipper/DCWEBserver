from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # 已有属性
    # id
    # password
    # last_login
    # is_superuser
    # username
    # first_name
    # last_name
    # email
    # is_staff
    # is_active
    # date_joined

    phone = models.CharField(max_length=20)
    num = models.CharField(max_length=20)
    gender = models.IntegerField(default=1)
    info = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        permissions = (
            ('user_management','用户管理'),
            ('group_management','角色管理'),
            ('permission_management','权限管理'),
            ('alarm_management', '报警管理'),
            ('report_management', '举报管理'),
            ('log_management', '日志管理'),
            ('grid_management', '网格管理'),
            ('device_management', '设备管理'),
            ('', ''),
        )


    def __str__(self):
        return str(self.username)
