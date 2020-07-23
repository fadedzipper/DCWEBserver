from django.db import models

# Create your models here.

#网格表
class Grid(models.Model):
    #网格名称
    name = models.CharField(max_length=100)
    #网格所在地
    location = models.CharField(max_length=100)
    #网格负责人
    leader = models.CharField(max_length=20)
    #负责人的联系方式
    telephone = models.IntegerField(default=0)


    def __str__(self):
        return str(self.name)









