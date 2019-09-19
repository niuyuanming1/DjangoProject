# Create your views here.
import json
import csv
from django.shortcuts import render, HttpResponse
from appname import testdb as test
import appname.user.user_manage as Users
from appname.game2048.url import GameView
from appname.entity_class.yun_dish import YunDish
from appname.mongodb.mongodb import Mongodb
from django.core import mail
from .models import Users as User
from threading import Thread
from appname.chat.chat_client import *
from appname.chat.chat_server import *
from appname.entity_class.result_manage import *
import socket as s
from socket import *


# def socket(request):
#     server_main(request)
#     res = {"status": 200}
#     return HttpResponse(json.dumps(res))
#
# def chat(request):
#     client_main(request)
#
#     res = {"status": 200}
#     return HttpResponse(json.dumps(res))
def export_csv(request):
    # 生成csv文本
    # 修改response的content-type头
    response = HttpResponse(content_type='text/csv')
    try:
        # 添加Content-Disposition头
        response['Content-Disposition'] = 'attachment;filename="allUser.csv"'
        all_user = User.objects.all()
        # 生成csv writer对象
        writer = csv.writer(response)
        # csv 表头
        # 可以为汉字
        writer.writerow(['ID', 'username', 'email', 'phone', 'pwd'])
        # 写具体数据
        for user in all_user:
            writer.writerow([user.id, user.userName, user.email, user.phoneNumber, user.passWord])
    except Exception as e:
        print(e)
    return response


def email(request):
    try:
        subject = eval(str(request.body, encoding="utf-8"))["title"]
        email = eval(str(request.body, encoding="utf-8"))["email"]
        message = eval(str(request.body, encoding="utf-8"))["content"]
        from_email = 'ding_t_f@163.com'
        arr = [email]
        mail.send_mail(
            subject,  # 题目
            message,  # 消息内容
            from_email,  # 发送者[当前配置邮箱]
            recipient_list=arr,  # 接收者邮件列表
            auth_password='gjy19881227'  # 在QQ邮箱->设置->帐户->“POP3/IMAP......服务” 里得到的在第三方登录QQ邮箱授权码
        )
        res = {"status": 200}
        return HttpResponse(json.dumps(res))
    except Exception as e:
        print(e)
        res = {"status": 404}
        return HttpResponse(json.dumps(res))


def index(request):
    return render(request, 'index.html')


def hello(request):
    test.testdb(request)
    data = request.body
    res = {
        "status": 200,
        "result": "Error",
    }
    return HttpResponse(json.dumps(res))


def login(request):
    if Users.login_user(request):
        res = {"status": 200}
    else:
        res = {"status": 400}
    return HttpResponse(json.dumps(res))


def register(request):
    if Users.add_user(request):
        res = {"status": 200}
    else:
        res = {"status": 400}
    return HttpResponse(json.dumps(res))


def homepage(request):
    active_user = Users.select_active_user(request)
    if active_user != None:
        res = {"status": 200,
               "email": active_user.email,
               "userName": active_user.userName,
               "phoneNumber": active_user.phoneNumber,
               "id": active_user.id,
               "passWord": active_user.passWord}
    else:
        res = {"status": 400}
    return HttpResponse(json.dumps(res))


def alluser(request):
    all_user_list = Users.select_all_user(request)
    if len(all_user_list) > 0:
        dict_user = {}
        i = 0
        for item in all_user_list:
            i += 1
            dict_user[i] = {"id": item.id, "email": item.email, "userName": item.userName,
                            "phoneNumber": item.phoneNumber,
                            "passWord": item.passWord}

        res = {"status": 200, "resule": dict_user}
    else:
        res = {"status": 400}
    return HttpResponse(json.dumps(res), content_type='application/json')


def deleteuser(request):
    if Users.delete_user(request):
        res = {"status": 200, "deleteid": eval(request.body.decode())["id"]}
    else:
        res = {"status": 400}
    return HttpResponse(json.dumps(res))


def updateuser(request):
    if Users.updateuser(request):
        res = {"status": 200}
    else:
        res = {"status": 400}
    return HttpResponse(json.dumps(res))


def game(request):
    view = GameView()
    map = view.start()
    res = {"status": 200, "result": map}
    return HttpResponse(json.dumps(res))


def updategame(request):
    user_input = eval(request.body)[0]  # 上38下40左 37右39
    last_list = eval(request.body)[1]
    view = GameView()
    map = view.update_map(user_input, last_list)
    res = {"status": 200, "result": map}
    return HttpResponse(json.dumps(res))


def yun(request):
    userName = eval(request.body.decode())["userName"]
    all_list = YunDish().select_all(userName)
    result_list = []
    for item in all_list:
        dict_ = {}
        dict_["id"] = item.id
        dict_["name"] = item.name
        dict_["url"] = item.url
        dict_["size"] = item.size
        dict_["userName"] = item.userName
        result_list.append(dict_)
    res = {"status": 200, "result": result_list}
    return HttpResponse(json.dumps(res))


def yun_insert(request):
    userName = eval(request.body.decode())["userName"]
    url = eval(request.body.decode())["url"]
    filename = eval(request.body.decode())["filename"]
    filesize = eval(request.body.decode())["size"]
    insert = YunDish().insert_one(filename, url, filesize, userName)
    if insert:
        res = {"status": 200}
    else:
        res = {"status": 400}
    return HttpResponse(json.dumps(res))


def yun_delete(request):
    fileid = eval(request.body.decode())["id"]
    delete = YunDish().delete(fileid)
    if delete:
        res = {"status": 200}
    else:
        res = {"status": 400}
    return HttpResponse(json.dumps(res))


def get_columnar_data(request):
    list_ = Mongodb().find_all()
    dict_ = {}
    for i in list_:
        dict_[i["书名"]] = i["评分"]
    res = {"status": 200, "result": dict_}
    return HttpResponse(json.dumps(res))
