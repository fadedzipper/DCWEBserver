from django.db import models
import datetime


class SysLog(models.Model):
    log_id = models.AutoField(primary_key=True,verbose_name='ID')
    log_addtime = models.DateTimeField(default=datetime.datetime.now,verbose_name="添加时间")
    log_type = models.CharField(max_length=20,verbose_name='日志类型')
    log_content = models.CharField(max_length=255,verbose_name='内容')
    log_user = models.CharField(max_length=255,verbose_name='操作人')
    log_ip = models.CharField(max_length=255,verbose_name='操作IP')
    log_dotype = models.CharField(max_length=20,verbose_name='操作方法',default='GET')
    class Meta:
        permissions = (
            ('users_syslog', '日志管理'),
        )