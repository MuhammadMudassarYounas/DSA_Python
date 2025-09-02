#Diameter of binary tree Leet code 543

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class tree:
    #Solution Using recursion
    def DiameterOfBinaryTree(self,node):
        self.diameter=0
        def Diameter(root):
            if root==None:
                return 0
            lS=Diameter(root.left)
            RS=Diameter(root.right)
            self.diameter=max(self.diameter,lS+RS)
            return 1+max(lS,RS)
        Diameter(node)
        return self.diameter

    
    

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
y=tree()
print(y.DiameterOfBinaryTree(five))
