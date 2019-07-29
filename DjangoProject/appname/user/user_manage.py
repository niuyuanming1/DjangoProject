from appname.models import User
import string
import ast
import json


def add_user(request):
    email = eval(str(request.body, encoding="utf-8"))["email"]
    userName = eval(str(request.body, encoding="utf-8"))["nickname"]

    num_email = User.objects.filter(email=email)
    num_userName = User.objects.filter(userName=userName)
    if len(num_email) < 1 and len(num_userName) < 1:
        passWord = eval(str(request.body, encoding="utf-8"))["password"]
        phoneNumber = int(eval(str(request.body, encoding="utf-8"))["phone"])
        jurisdiction = True  # 普通用户
        user = User(email=email, passWord=passWord, userName=userName, phoneNumber=phoneNumber,
                    jurisdiction=jurisdiction)
        user.save()
        return True
    return False


def login_user(request):
    userName = eval(request.body.decode())["email"]
    password = eval(request.body.decode())["password"]
    sql_email = User.objects.filter(email=userName)
    if len(sql_email) >= 1:
        sql_password = sql_email[0].passWord
        if len(sql_email) == 1 and password == sql_password:
            return True
    return False


def select_active_user(request):
    active_user_email = request.body.decode()[8:].replace("\"", "")
    sql_active_user = User.objects.filter(email=active_user_email)
    if len(sql_active_user)>=1:
        return sql_active_user[0]
    return None

def select_all_user(request):
    return User.objects.all()

def delete_user(request):
    user1 = User.objects.get(id=eval(request.body.decode())["id"])
    user1.delete()
    return True

def updateuser(request):
    user1 = User.objects.get(id=eval(request.body.decode())["id"])
    if type(user1) == User:
        user1.userName = eval(request.body.decode())["userName"]
        user1.email = eval(request.body.decode())["email"]
        user1.passWord = eval(request.body.decode())["passWord"]
        user1.phoneNumber = eval(request.body.decode())["phoneNumber"]
        user1.save()
        return True
    return False

