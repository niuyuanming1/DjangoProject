"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appname import views as app_views
from django.conf.urls import url

urlpatterns = [
        path('', app_views.index),
        path('admin/', admin.site.urls),
        path('hello/', app_views.hello),
        path('login/', app_views.login),
        path('register/', app_views.register),
        path('homepage/', app_views.homepage),
        path('alluser/', app_views.alluser),
        path('deleteuser/', app_views.deleteuser),
        path('updateuser/', app_views.updateuser),
        path('game/', app_views.game),
        path('updategame/', app_views.updategame),
        # path('socket/', app_views.socket),
        # path('chat/', app_views.chat),
        path('yundish/', app_views.yun),
        path('yuninsert/', app_views.yun_insert),
        path('yundelete/', app_views.yun_delete),
        path('get_columnar_data/', app_views.get_columnar_data),
        url(r'^email/$',app_views.email),
        url(r'^export/$',app_views.export_csv),

]
