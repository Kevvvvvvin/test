class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None

class SLL(object):
    def __init__(self):
        self.head=None
    def is_empty(self):
        return self.head is None
    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
    def solution(self):
        cur = self.head
        while cur.next is not None:
            next = cur.next.next
            node1 = Node(cur.item)
            node2 = Node(cur.next.item)
            node2.next = node1
            node1.next = cur.next.next
            print(node1.item,node2.item)
            if cur ==self.head:
                self.head = node2
                cur = next
            else:
                cur = next

    def items(self):
        cur = self.head
        while cur is not None:
            yield cur.item
            cur = cur.next

s = [1,2,3,4,5]
s_linked = SLL()
for i in s:
    s_linked.append(i)
s_new = []
for i in s_linked.items():
    s_new.append(i)
i = 0
while i< len(s_new)-1:
    s_new[i],s_new[i+1]=s_new[i+1],s_new[i]
    i+=2
s_linked_new = SLL()
for i in s_new:
    s_linked_new.append(i)
for i in s_linked_new.items():
    print(i,end=' ')



