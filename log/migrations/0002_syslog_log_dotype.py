# Generated by Django 2.2.6 on 2020-07-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='syslog',
            name='log_dotype',
            field=models.CharField(default='GET', max_length=20, verbose_name='操作方法'),
        ),
    ]