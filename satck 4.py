class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return None
        value = self.head.data
        self.head = self.head.next
        return value

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.head.data


stack = LinkedStack()

stack.push(7)
stack.push(14)
stack.push(21)

print("Top element:", stack.peek())

print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Popped:", stack.pop())
stack.pop()