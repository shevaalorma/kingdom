class SingleNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        # self.prev = prev

    def __repr__(self):
        return str(self.val)

    def __str__(self):
        return str(self.val)

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        if item is SingleNode:
            node = item
        else:
            node = SingleNode(item)

        prev = self.tail
        if self.head is None:
            self.head = node
        else:
            prev.next = node
        self.tail = node

    def iternodes(self):
        current = self.head
        while current:
            yield current
            current = current.next

node= SingleNode(5)
ll = Linked_list()
ll.append(node)
node= SingleNode(7)
ll.append(node)
for i in ll.iternodes():
    print(i)
