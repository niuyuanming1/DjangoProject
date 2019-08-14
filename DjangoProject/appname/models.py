# Create your models here.
from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50, default='title')
    content = models.TextField(null=True)
class Brticle(models.Model):
    title = models.CharField(max_length=50, default='title')
    content = models.TextField(null=True)
# 邮箱，密码，昵称，电话，(必填), 权限
class Users(models.Model):
    email = models.EmailField(max_length=30,null=True)  # 邮箱
    passWord = models.CharField(max_length=30, null=True)  # 密码
    userName = models.CharField(max_length=40, null=True)  # 用户名
    phoneNumber = models.BigIntegerField(null=True)  # 电话
    jurisdiction = models.BooleanField(null=False)  # 权限 0：管理员 1：普通用户
