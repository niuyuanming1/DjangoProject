import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

# dblist = myclient.list_database_names()
# if "直播" in dblist:
#  print("数据库已存在！")
mydb = myclient["直播"]

# collist = mydb. list_collection_names()
# if "test" in collist:   # 判断 sites 集合是否存在
#  print("集合已存在！")
mycol = mydb["test"]


class Mongodb:
    def __init__(self):
        pass

    # 查询所有的内容
    def find_all(self):
        list_ = []
        for i in mycol.find():
            list_.append(i)
        return list_
