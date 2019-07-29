class LStack:
    def __init__(self):
        self.__top = None
    def is_empty(self):
        return self.__top is None
    def push(self,val):
        node = Node(val)
        node.next = self.__top
        self.__top = node
    def pop(self):
        if self.is_empty():
            raise StackError("pop from empty stack")
        data = self.__top.val
        self.__top = self.__top.next
        return data
    def top(self):
        if self.is_empty():
            raise StackError("pop from empty stack")
        return self.__top.val



class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class StackError(Exception):
        pass

if __name__ == '__main__':
    ls = LStack()
    ls.push(1)
    ls.push(2)
    ls.pop()
    print(ls.top())