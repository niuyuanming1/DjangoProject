from appname.game2048.bll import GameController
from appname.game2048.model import MoveDirection


class GameView:
    def __init__(self):
        self.__controller = GameController()
    def start(self):
        self.__controller.random_num()
        self.__controller.random_num()
        return self.__controller.map
    def update_map(self,num,list):
        while True:
            #　获取输入
            self.__controller.map=list
            self.get_input(num)
            if not self.__controller.is_change: return list
            self.__controller.random_num()
            if self.__controller.game_end():
                # 如果结束则退出循环
                print("游戏结束喽")
                break
            return self.__controller.map
    def get_input(self,num):
        str_input = num
        # 移动地图
        if str_input == 38:
            self.__controller.move(MoveDirection.UP)
        elif str_input == 40:
            self.__controller.move(MoveDirection.DOWN)
        elif str_input == 37:
            self.__controller.move(MoveDirection.LEFT)
        elif str_input == 39:
            self.__controller.move(MoveDirection.RIGHT)