class SingleNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

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
            node.prev = self.tail
        self.tail = node

    def iternodes(self, reverse=False):
        current = self.tail if reverse else self.head
        while current:
            yield current
            current = current.prev if reverse else current.next

    def insert(self, index, val):
        if index < 0:
            return ValueError('Wrong Index{}'.format(index))

        current = None
        for i, node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break

        # 没找到
        if current is None:
            self.append(val)
            return

        node = SingleNode(node)
        prev = current.prev
        next = node.next

        # 找到了
        if prev is None:  # ==1
            self.head = node
        else:  # >1
            prev.next = node
            node.prev = prev

        current.prev = node
        node.next = current

    def pop(self):
        if self.tail is None:  # 空的
            raise Exception('Empty')

        node = self.tail
        val = node.val
        prev = node.prev

        if prev is None:  # == 1
            self.tail = None
            self.head = None
        else:  # >  1
            prev.next = None
            self.tail = prev
        return val

    def remove(self,index):
        if self.tail is None:
            raise Exception('Empty')
        if index < 0 :
            raise ValueError('Wrong Index{}'.format(index))

        current = None
        for i,node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        if current is None:# 没找到
            raise ValueError('Wrong Index{}'.format(index))

        prev = current.prev
        next = current.next

        if prev is None and next is None:# ==1
            self.tail = None
            self.head = None
        elif prev is None:
            self.head = next
            next.prev = None
        elif next is None:
            self.tail = prev
            prev.next = None
        else:
            prev.next = next
            next.prev = prev




ll = LinkedList()
ll.append('1')
ll.append('2')
ll.append('3')
ll.append('4')
ll.append('5')
print(ll.head, ll.tail)
ll.insert(100, '6')
ll.pop()
ll.pop()
ll.pop()
ll.remove(1)
for x in ll.iternodes():
    print(x)
