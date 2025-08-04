class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Doubly_Linked_List:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data,end=" <---> ")
            temp=temp.next
        print()
    def Reverse(self):
        curr=self.head
        prev=None
        while curr is not None:
            front=curr.next
            curr.next=prev
            curr.prev=front
            prev=curr
            curr=front
            self.head=prev
        
dll=Doubly_Linked_List()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)
dll.append(60)
print("Original List ")
dll.print_list()

dll.Reverse()

print("Reverse List")
dll.print_list()