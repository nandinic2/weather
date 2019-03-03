class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        print(self.items)

s = Stack()
s.push('I')
s.push(' really')
s.push(' love')
s.push(' ice cream.')
s.peek()

print(s)



class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self, item):
        self.items.pop()

    def peek(self):
        print(self.items)

q = Queue()
q.enqueue('I')
q.enqueue('love')
q.enqueue('ice cream')
q.peek()

print(q)

for x in s:
    new_arr = []
