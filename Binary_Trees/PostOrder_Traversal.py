#leet code problem 

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def PostOrder(node):
    if node==None:
        return
    PostOrder(node.left)
    PostOrder(node.right)
    print(node.val,end=" ")

#Make obj
one=Node(1)
two=Node(2)
three=Node(3)
four=Node(4)
five=Node(5)
six=Node(6)
seven=Node(7)
eight=Node(8)
nine=Node(9)
ten=Node(10)
#all node connect each other

five.left=three
five.right=four

three.left=two
three.right=nine

four.left=eight
four.right=ten

eight.left=one
eight.right=six

PostOrder(five)
