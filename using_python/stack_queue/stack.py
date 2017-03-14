class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
       return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

stack = Stack()
print("*"*50)
print(stack.size())

print("*"*50)
for i in range(0,10):
    stack.push(i)
print(stack.size())
print("*"*50)
print(stack.peek())
print("*"*50)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("*"*50)
print(stack.size())
print(stack.peek())
