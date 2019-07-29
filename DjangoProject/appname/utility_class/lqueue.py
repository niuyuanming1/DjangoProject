class LQueue:
    def __init__(self):
        self.__front = self.__rear = Node(None)

    def is_empty(self):
        return self.__front == self.__rear

    def enqueue(self, val):
        node = Node(val)
        self.__rear.next = node
        self.__rear = node

    def dequeue(self):
        if self.is_empty():
            raise QueueError("queue is empty")
        self.__front = self.__front.next
        return self.__front.val


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class QueueError(Exception):
    pass


if __name__ == '__main__':
    lq = LQueue()
    lq.enqueue(1)
    lq.enqueue(2)
    print(lq.dequeue())
    print(lq.dequeue())