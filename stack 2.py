class BoundedStack:
    def __init__(self, capacity):
        self.arr = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.arr) == 0

    def is_full(self):
        return len(self.arr) == self.capacity

    def push(self, value):
        if self.is_full():
            print(f"Stack overflow, cannot push {value}")
            return
        self.arr.append(value)

    def pop(self):
        if self.is_empty():
            print("Stack underflow, cannot pop")
            return None
        return self.arr.pop()


stack = BoundedStack(3)

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Popped:", stack.pop())
stack.pop()