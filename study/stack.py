""" 
자료구조 - 스택
"""

class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        del self.stack[-1]
    
    def read(self):
        return self.stack
    


if __name__ == "__main__":
    stack = MyStack()

    stack.push(3)
    stack.push(4)
    stack.push(22)
    print(stack.read())
    stack.pop()
    print(stack.read())



