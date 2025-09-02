class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def PreOrder(node):
    if node==None:
        return
    print(node.val,end=" ")
    PreOrder(node.left)
    PreOrder(node.right)

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

PreOrder(five)
