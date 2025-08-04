class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class Doubly_Linked_List:
    def __init__(self):
        self.head=None
    def Insert_at_Head(self,val):
        new_node=Node(val)
        if not self.head:
            new_node=self.head
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    def insert_at_Last(self,val):
        new_node=Node(val)
        if not self.head:
            new_node=self.head
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
            new_node.prev=current
            print(current.val)
    def insert_at_between(self,val,position):
        new_node=Node(val)
        if position==0:
            self.Insert_at_Head(val)
            return
        current=self.head
        count=0
        while current and count<position-1:
            current=current.next
            count+=1
        if current is None:
            print("Position out of bound ")
            return
        new_node.next=current.next
        new_node.prev=current
        if current.next:
            current.next.prev=new_node
        current.next=new_node
    def Print(self):
        if self.head==None:
            print("doubly linked list is empty")
        else:
            curr=self.head
            while curr is not None:
                print(curr.val,end=" ")
                curr=curr.next
            print()

DLL=Doubly_Linked_List()
DLL.insert_at_Last(10)
DLL.insert_at_Last(20)
DLL.insert_at_Last(30)
DLL.insert_at_Last(40)
DLL.Print()