class SingleNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return repr(self.val)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        if item is SingleNode:
            node = item
        else:
            node = SingleNode(item)

        prev = self.tail
        if prev is None:
            self.head = node
        else:
            prev.next = node
        self.tail = node

    def iternodes(self, reverse=False):
        current = self.head
        while current:
            yield current
            current = current.next


ll = LinkedList()
ll.append('1')
ll.append('2')
ll.append('3')
ll.append('4')
ll.append('5')
print(ll.head,ll.tail)
for x in ll.iternodes():
    print(x)

