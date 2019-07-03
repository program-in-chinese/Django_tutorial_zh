import datetime

from django.db import models
from django.utils import timezone

class 问题(models.Model):
    内容 = models.CharField(max_length=200)
    发问日期 = models.DateTimeField('发布问题日期')

    def __str__(self):
        return self.内容

    def 刚发问(self):
        return self.发问日期 >= timezone.now() - datetime.timedelta(days=1)

class 选项(models.Model):
    问题 = models.ForeignKey(问题, on_delete=models.CASCADE)
    内容 = models.CharField(max_length=200)
    票数 = models.IntegerField(default=0)

    def __str__(self):
        return self.内容
