class Queue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def enqueue(self, value):
        self.elements.insert(0, value)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.elements.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.elements[-1]


class Stack:
    def __init__(self):
        self.elements = Queue()

    def is_empty(self):
        return self.elements.is_empty()

    def push(self, value):
        self.elements.enqueue(value)

    def pop(self):
        for i in range(len(self.elements.elements) - 1):
            self.elements.enqueue(self.elements.dequeue())
        return self.elements.dequeue()

    def top(self):
        for i in range(len(self.elements.elements) - 1):
            self.elements.enqueue(self.elements.dequeue())
        return_val = self.elements.peek()
        self.elements.enqueue(self.elements.dequeue())
        return return_val


s = Stack()
s.push(4)
s.push(3)
s.push(2)
s.push(1)
print(s.pop())
print(s.top())
print(s.pop())
print(s.pop())
print(s.pop())

OUTPUT:
1
2
2
3
4