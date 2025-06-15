#Implement a stack with push, pop, and peek
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
      if self.is_empty():
        print("Stack is empty")
      else:
        print("Stack elements are:", self.items)
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack after filling the stack :",stack.display() ) 
print("Peek in the stack:", stack.peek())  
print("After 1st Pop,the element removed:", stack.pop())  
stack.display()  
print("After 2nd Pop,the element removed::", stack.pop())
print("After 3rd Pop,the element removed::", stack.pop())
print("After 4th Pop,the element removed::", stack.pop()) 
print("After all Pops:",stack.display())
