from .models import SysLog

# log_id = models.AutoField(primary_key=True, verbose_name='ID')
# log_addtime = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")
# log_type = models.CharField(max_length=20, verbose_name='日志类型')
# log_content = models.CharField(max_length=255, verbose_name='内容')
# log_user = models.CharField(max_length=255, verbose_name='操作人')
# log_ip = models.CharField(max_length=255, verbose_name='操作IP')

def addlog(request,log_type,log_content,log_dotype):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        # username = "Anonymous"
        username = "匿名用户"
    ip = request.META.get('REMOTE_ADDR', '0.0.0.0')

    SysLog.objects.create(log_type=log_type,log_user=username,log_content=log_content,log_ip=ip,log_dotype=log_dotype)
#还没同步其他模块
