# -*- coding: utf-8 -*-

from django.http import HttpResponse

from appname.models import Article


# 数据库操作
def testdb(request):
    a = Article(title="sssss",content='fffff')
    a.save()
    # 初始化
    response = ""
    response1 = ""
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Article.objects.all()
    for item in list:
        print(item)
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    # response2 = Article.objects.filter(id=1)
    # response2(name="niu")
    # 获取单个对象
    # response3 = Article.objects.get(id=1)
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    # Article.objects.order_by('name')[0:2]
    # 数据排序
    # Article.objects.order_by("id")
    # 上面的方法可以连锁使用
    # Article.objects.filter(name="runoob").order_by("id")
    # 输出所有数据
    # for var in list:
    #     response1 += var.name + " "
    # response = response1
    return HttpResponse("<p>" + response + "</p>")