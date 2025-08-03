class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Single_Linked_List:
    def __init__(self):
        self.head=None
    def Append(self,val):
        new_Node=Node(val)
        if self.head==None:
            self.head=new_Node
        else:
            curr =self.head
            while curr.next is not None:
                curr= curr.next
            curr.next=new_Node
             
    def Traversal(self):
        if self.head==None:
            print("Single linked list is empty")
        else:
            curr=self.head
            while curr is not None:
                print(curr.val,end=" ")
                curr=curr.next
    def insert_Value(self,val,position):
        new_node=Node(val)
        if position==0:
            new_node.next=self.head
            self.head==new_node
        else:
            prev=None
            curr=self.head
            count=0
            while curr is not None and count<position:
                prev=curr
                curr=curr.next
                count+=1
            prev.next=new_node
            new_node.next=curr
    def Delete_Value(self,value):
        temp=self.head
        if temp.next is  not None:
            if temp.val==value:
                self.head=self.head.next
                temp.next=None
                del temp
                return
            else:
                prev=None
                found=False
                while temp is not None:
                    if temp.val==value:
                        found=True
                        break
                    prev=temp
                    temp=temp.next
                if found:
                    prev.next=temp.next
                    temp.next=None
                    del temp
                    return
                else:
                    print("Element not exist")

sll= Single_Linked_List()
sll.Append(10)
sll.Append(20)
sll.Append(30)  
sll.Append(40)
sll.Append(50)
sll.Traversal()
sll.Delete_Value(40)
sll.Traversal()
