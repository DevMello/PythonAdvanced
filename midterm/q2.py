class Queue:
        def __init__(self):
            self.enqueue_stack = []
            self.dequeue_stack = []

        def len(self):
            return len(self.enqueue_stack) + len(self.dequeue_stack)

        def is_empty(self):
            return len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0

        def top(self):
            if len(self.dequeue_stack) == 0:
                while len(self.enqueue_stack) > 0:
                    self.dequeue_stack.append(self.enqueue_stack.pop())
            return self.dequeue_stack[-1]

        def enqueue(self, item):
            self.enqueue_stack.append(item)

        def dequeue(self):
            if len(self.dequeue_stack) == 0:
                while len(self.enqueue_stack) > 0:
                    self.dequeue_stack.append(self.enqueue_stack.pop())
            if len(self.dequeue_stack) == 0:
                return None
            return self.dequeue_stack.pop()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue(6)
q.enqueue(7)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue(8)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())