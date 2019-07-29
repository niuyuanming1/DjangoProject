class SQueue:
    def __init__(self):
        self.__elems = []
    def is_empty(self):
        return self.__elems == []
    def enqueue(self,val):
        self.__elems.append(val)
    def dequeue(self):
        if self.is_empty():
            raise QueueError("queue is empty")
        return self.__elems.pop(0)

class QueueError(Exception):
    pass

if __name__ == '__main__':
    sq = SQueue()
    sq.enqueue(1)
    sq.enqueue(2)
    print(sq.dequeue())
    print(sq.dequeue())