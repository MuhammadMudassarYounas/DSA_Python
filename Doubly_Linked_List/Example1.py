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
    def PairSum(self,target):
        Result=[]
        left=self.head
        Right=self.head
        while Right.next is not None:
            Right=Right.next
        while left is not None and Right is not None and left.data <= Right.data:
            total=left.data + Right.data
            if total ==target:
                Result.append([left.data,Right.data])
                left=left.next
                Right=Right.prev
            elif total >target:
                Right=Right.prev
            else:
                left=left.next
        print(Result)

dll=Doubly_Linked_List()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(3)
dll.append(6)
dll.append(6)
dll.append(9)
dll.PairSum(7)