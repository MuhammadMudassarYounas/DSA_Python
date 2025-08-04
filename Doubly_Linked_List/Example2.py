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
    def removeDuplicate(self):
        curr=self.head
        while curr.next is not None:
            if curr.prev ==self.head:
                curr.prev=None
                self.head=curr
            if curr.data==curr.prev.data:
                curr.prev.prev.next=curr
                curr.prev=curr.prev.prev
            curr=curr.next
dll=Doubly_Linked_List()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(3)
dll.append(6)
dll.append(6)
dll.append(9)
dll.removeDuplicate()
dll.print_list()