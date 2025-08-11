class QueueUsingArray:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items)==0:
            print("Queue is empty")
            return
        return self.items.pop(0)
    def front(self):
        return self.items[0]
    def rear(self):
        return self.items[-1]
    
QUL=QueueUsingArray()
QUL.enqueue(5)
QUL.enqueue(10)
QUL.enqueue(15)
QUL.enqueue(20)
print(QUL.dequeue())
print(QUL.front())