""" 
자료구조 - 큐 구현
"""

class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        del self.queue[0]
    
    def read(self):
        return self.queue
    

if __name__ == "__main__":
    myQueue = MyQueue()

    myQueue.enqueue(4)
    myQueue.enqueue(3)
    myQueue.enqueue(16)
    myQueue.enqueue(42)
    myQueue.enqueue(12)
    myQueue.enqueue(7)
    print(myQueue.read())
    myQueue.dequeue()
    print(myQueue.read())
