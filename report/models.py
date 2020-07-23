from django.db import models

# Create your models here.

class Report(models.Model):

    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    topic = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    handled = models.IntegerField(default=0)
    info = models.CharField(max_length=500)
    handle_content = models.CharField(null=True, default="", max_length=500)


