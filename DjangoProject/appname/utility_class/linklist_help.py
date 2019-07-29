class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkList:
    def __init__(self):
        self.head = Node(None)
    def init_list(self,list_):
        p = self.head
        for i in list_:
            p.next = Node(i)
            p = p.next
    def show_link(self,list_):
        p = self.head
        while p.next is not None:
            print(p.next.val)
            p = p.next
    def append(self,val):
        p = self.head
        while p.next is not None:
            p = p .next
        p.next = Node(val)
    def head_insert(self,val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
    def insert(self,index,val):
        p = self.head
        for i in range(index):
            if p.next is None:
                break
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node
    def remove(self,val):
        p = self.head
        while p.next.val != val and p.next is not None:
            p = p.next
        if p.next is None:
            raise ValueError("x not in linklist")
        else:
            p.next = p.next.next
    def search(self,index):
        if index < 0:
            raise ImportError("index out of range")
        p = self.head
        for i in range(index):
            if p.next is None:
                raise ImportError("index out of range")
            p = p.next
        return p.next.val





if __name__ == "__main__":
    ls = []
    for i in range(10):
        ls.append(i)
    link = LinkList()
    link.init_list(ls)
    link.append(111)
    link.head_insert(222)
    link.insert(2,3333)
    link.remove(3333)
    print(link.search(0))
    link.show_link(ls)
