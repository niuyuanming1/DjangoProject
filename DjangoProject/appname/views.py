# Create your views here.
import json
from django.shortcuts import render, HttpResponse
from appname import testdb as test
import appname.user.user_manage as User
from appname.game2048.url import GameView


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
    if User.login_user(request):
        res = {"status": 200}
    else:
        res = {"status": 400}
    return HttpResponse(json.dumps(res))


def register(request):
    if User.add_user(request):
        res = {"status": 200}
    else:
        res = {"status": 400}
    return HttpResponse(json.dumps(res))


def homepage(request):
    active_user = User.select_active_user(request)
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
    all_user_list = User.select_all_user(request)
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
    return HttpResponse(json.dumps(res))


def deleteuser(request):
    if User.delete_user(request):
        res = {"status": 200, "deleteid": eval(request.body.decode())["id"]}
    else:
        res = {"status": 400}
    return HttpResponse(json.dumps(res))


def updateuser(request):
    if User.updateuser(request):
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
    map = view.update_map(user_input,last_list)
    res = {"status": 200, "result": map}
    return HttpResponse(json.dumps(res))