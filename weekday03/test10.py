class DoubleNode():
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next= next

    def __repr__(self):
        return str(self.val)

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        if item is DoubleNode:
            node = item
        else:
            node = DoubleNode(item)
        current = self.tail
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        node = self.tail

    def iternodes(self,reversal = False):
        current =self.tail if reversal else self.head
        while current:
            yield current
            current = current.prev if reversal else current.next

ll = LinkedList()
node = DoubleNode(5)
ll.append(node)
node = DoubleNode(7)
ll.append(node)
node = DoubleNode(5)
ll.append(node)
node = DoubleNode(5)
ll.append(node)
for i in ll.iternodes():
    print(i)