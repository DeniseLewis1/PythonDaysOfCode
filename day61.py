# Create a program to implement a stack using a list

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.get_size() > 0:
            return self.stack.pop()
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0
    
    def get_size(self):
        return len(self.stack)
    
    def peek(self):
        if self.get_size() > 0:
            return self.stack[-1]
        else:
            print("Stack is empty")

    def show_stack(self):
        return self.stack        


new_stack = Stack()

for i in range(6):
    new_stack.push(i)

print(f"Stack: {new_stack.show_stack()}")

for i in range(3):
    print(f"Popped from stack: {new_stack.pop()}")

print(f"Stack: {new_stack.show_stack()}")

print(f"Stack empty: {new_stack.is_empty()}")
print(f"Size of stack: {new_stack.get_size()}")
print(f"Top of stack: {new_stack.peek()}")
