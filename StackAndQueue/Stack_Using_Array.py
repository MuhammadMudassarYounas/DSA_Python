class stackUsingArray:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if len(self.items)==0:
            print("Stack is Empty")
        x=self.items.pop()
        return x
    def top(self):
        if len(self.items)==0:
           return print("Stack is Empty")
        return self.items[-1]
    def size(self):
        return len(self.items)
    
SUL=stackUsingArray()
SUL.push(5)
SUL.push(10)
SUL.push(15)
SUL.push(20)
SUL.push(25)
print(SUL.top())
SUL.pop()
print(SUL.top())
