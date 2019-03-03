class Stack():

    def __init__(self):
        self.items = []

    def isEmpty(self):
        # return a boolean
        return self.items == []

    def push(self,item):
        self.items.append(item)

# create an instance of the class
stacky = Stack()
stacky.push('hello')
print(stacky.isEmpty())
