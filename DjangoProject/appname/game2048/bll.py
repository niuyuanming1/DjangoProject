import copy
import random

from appname.game2048.model import MoveDirection


class GameController:
    def __init__(self):
        self.__list_merge = [2, 16, 0, 4]
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.__list_empty = []
        self.__is_change = False

    @property
    def is_change(self):
        return self.__is_change

    @property
    def map(self):
        return self.__map
    @map.setter
    def map(self,value):
        self.__map = value

    def __zero_to_end(self):
        # 思想：从后向前，如果是零元素，删除后末尾追加零.
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    # 2. 定义合并相同元素的函数
    # [2,2,0,0]  --> [4,0,0,0]
    # [2,0,0,2]  --> [4,0,0,0]
    # [2,0,2,2]  --> [4,2,0,0]
    # [0,2,2,4]  --> [4,4,0,0]
    # [2,2,2,2]  --> [4,4,0,0]
    # 14：32
    def __merge(self):
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):  # 0  1  2
            # 如果相邻 还 相同
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] *= 2
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    # merge()
    # print(list_merge)
    # 3. 向左移动
    def move_left(self):
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    # move_left()
    # print(map)
    # 4. 向右移动
    def move_right(self):
        for line in self.__map:
            # 切片会产生新列表
            self.__list_merge = line[::-1]
            # 合并操作的就是新列表
            self.__merge()
            # 将新列表中的数据赋值给map中的行
            line[::-1] = self.__list_merge

    # move_right()
    # print(map)

    # 5. 向上移动
    def move_up(self):
        self.__square_matrix_transpose()
        self.move_left()
        self.__square_matrix_transpose()

    # 6. 向下移动

    def move_down(self):
        self.__square_matrix_transpose()
        self.move_right()
        self.__square_matrix_transpose()

    def __square_matrix_transpose(self):
        """
            矩阵转置
        """
        for c in range(1, len(self.__map)):
            for r in range(c, len(self.__map)):
                self.__map[r][c - 1], self.__map[c - 1][r] = self.__map[c - 1][r], self.__map[r][c - 1]

    def random_num(self):
        num = 2
        if random.randint(0, 10) == 4:
            num = 4

        self.get_blank()
        if len(self.__list_empty) == 0: return
        tuple1 = random.randint(0, len(self.__list_empty) - 1)
        self.__map[self.__list_empty[tuple1][0]][self.__list_empty[tuple1][1]] = num
        # self.__list_empty.remove(tuple1)

    def get_blank(self):
        self.__list_empty.clear()
        for r in range(0, len(self.__map)):
            for c in range(0, len(self.__map[r])):
                if self.__map[r][c] == 0:
                    self.__list_empty.append((r, c))

    def level_identical(self):
        for r in range(0, len(self.__map)):
            for c in range(0, len(self.__map[r])):
                if self.__map[c] == self.__map[c + 1]:
                    return True

    def vertical_identical(self):
        self.__square_matrix_transpose()
        for r in range(0, len(self.__map)):
            for c in range(0, len(self.__map[r])):
                if self.__map[c] == self.__map[c + 1]:
                    return True

    def move(self, dir=MoveDirection.UP):
        # 移动前记录地图
        original_map = copy.deepcopy(self.__map)

        if dir == MoveDirection.UP:
            self.move_up()
        elif dir == MoveDirection.DOWN:
            self.move_down()
        elif dir == MoveDirection.LEFT:
            self.move_left()
        elif dir == MoveDirection.RIGHT:
            self.move_right()

        # 移动后进行比较
        self.__is_change = self.__map != original_map
        # true 表示有变化(不相等)  false 表示没变化(相等)

    def game_end(self):
        if len(self.__list_empty) != 0 or self.level_identical() or self.vertical_identical():
            pass
    # move_down()
    # print(map)
