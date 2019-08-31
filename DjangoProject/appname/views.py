# Create your views here.
import json
from django.shortcuts import render, HttpResponse
from appname import testdb as test
import appname.user.user_manage as Users
from appname.game2048.url import GameView
from appname.entity_class.yun_dish import YunDish
from appname.mongodb.mongodb import Mongodb
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
    return JsonRespons


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
    insert = YunDish().insert_one(filename,url,filesize,userName)
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
        dict_[i["书名"]]=i["评分"]
    res = {"status": 200, "result": dict_}
    return HttpResponse(json.dumps(res))