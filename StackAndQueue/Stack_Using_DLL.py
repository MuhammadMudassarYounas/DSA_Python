class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
        self.tail=None
class StackUsingDoublyLinkedList:
    def __init__(self):
         self.head=None
    def push(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail=new_node
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node

    def pop(self):
        return self.tail.val
    def Print(self):
        if self.head==None:
            print("doubly linked list is empty")
        else:
            curr=self.head
            while curr is not None:
                print(curr.val,end=" ")
                curr=curr.next
            print()

SUL=StackUsingDoublyLinkedList()
SUL.push(1)
SUL.push(2)
SUL.push(3)
SUL.push(4)
print(SUL.pop())
SUL.Print()


