class ArrayStack:
    def __init__(self, capacity=100):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, value):
        if self.is_full():
            print("Stack overflow")
            return
        self.top += 1
        self.arr[self.top] = value

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return None
        value = self.arr[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.arr[self.top]

    def size(self):
        return self.top + 1


stack = ArrayStack()

stack.push(5)
stack.push(15)
stack.push(25)

print("Current size:", stack.size())
print("Top element:", stack.peek())

stack.pop()
print("Size after pop:", stack.size())
print("Top element now:", stack.peek())