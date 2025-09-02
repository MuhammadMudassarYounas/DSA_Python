class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

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
eleven=Node(11)
Fourteen=Node(14)
Fifteen=Node(15)

nine.left=three
nine.right=eleven

three.left=two
three.right=seven

seven.left=four
seven.right=eight

eleven.right=Fifteen
Fifteen.left=Fourteen

print(nine.left.right.right.val)
