class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def pop(self):
        if self.head:
            item = self.head.item
            self.head = self.head.next
            return item
        raise ValueError('Queue is empty.')

    @property
    def peek(self):
        return self.head.item

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        s = ''
        current = self.head
        while current is not None:
            s += str(current.item)+' '
            current = current.next
        return f'start -> {s}<- end'

class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q1.add(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.add(self.q1.pop())
        item = self.q1.pop()
        self.q1, self.q2 = self.q2, self.q1
        return item

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.add(self.q1.pop())
        item = self.q1.peek
        self.q2.add(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1
        return item

    def empty(self) -> bool:
        return self.q1.is_empty() and self.q2.is_empty()