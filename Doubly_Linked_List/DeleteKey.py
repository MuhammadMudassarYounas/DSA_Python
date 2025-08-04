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
    def Delete(self,k):
        if self.head is None and self.head.val==k:
            return None
        temp=self.head
        prev=None
        new_head=self.head
        while prev is not None:
            if temp.val==k:
                if prev is not None:    
                    prev.next=temp.next
                if temp.next is not None:
                    temp.next.prev=prev
                if temp ==new_head:
                    new_head=new_head.next
            prev=temp
            temp=temp.next
dll=Doubly_Linked_List()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(20)
dll.append(60)
print("Original List ")
dll.print_list()
dll.Delete(20)
print("After ")
dll.print_list()