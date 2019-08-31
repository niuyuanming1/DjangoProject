from appname.models import Yundish


class YunDish:
    def __init__(self):
        pass

    def select_all(self,userName):
        return Yundish.objects.filter(userName=userName)
    def insert_one(self,name,url,size,userName):
        old_url = Yundish.objects.filter(url=url)
        if len(old_url) < 1:
            yun = Yundish(name=name,url=url,size=size,userName=userName)
            yun.save()
            return True
        return False
    def delete(self,id):
        yun = Yundish.objects.get(id=id)
        yun.delete()
        return True



