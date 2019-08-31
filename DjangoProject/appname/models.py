# Create your models here.
from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50, default='title')
    content = models.TextField(null=True)


class Brticle(models.Model):
    title = models.CharField(max_length=50, default='title')
    content = models.TextField(null=True)


# 邮箱，密码，昵称，电话， 权限(必填),
class Users(models.Model):
    email = models.EmailField(max_length=30, null=True)  # 邮箱
    passWord = models.CharField(max_length=30, null=True)  # 密码
    userName = models.CharField(max_length=40, null=True)  # 用户名
    phoneNumber = models.BigIntegerField(null=True)  # 电话
    jurisdiction = models.BooleanField(null=False)  # 权限 0：管理员 1：普通用户

#文件名、文件地址。文件大小以MB为单位
class Yundish(models.Model):
    userName = models.CharField(max_length=40, null=True)  # 用户名
    name = models.CharField(max_length=50)  # 文件名
    url = models.CharField(max_length=500) # 文件地址
    size = models.FloatField(null=True)  # 文件的大小
