class SStack:
    def __init__(self):
        self.__elems = []

    def is_empty(self):
        return self.__elems == []

    def push(self, val):
        self.__elems.append(val)

    def pop(self):
        if self.is_empty():
            raise StackError("pop from empty stack")
        return self.__elems.pop()

    def top(self):
        if self.is_empty():
            raise StackError("pop from empty stack")
        return self.__elems[-1]


class StackError(Exception):
    pass


if __name__ == '__main__':
    ss = SStack()
    ss.push(1)
    ss.push(2)
    ss.pop()
    print(ss.top())
