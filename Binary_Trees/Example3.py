#binary tree is balance are not Leet code 

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Tree:
    def BalancedOfBinaryTree(self,node):
        def solve(root):
            if root==None:
                return 0
            LS=solve(root.left)
            if LS==-1:
                return -1
            RS=solve(root.right)
            if RS == -1:
                return -1
            if abs(LS-RS)>1:
                return -1
            return 1+max(LS,RS)
        x=solve(node)
        if x==-1:
            return False
        return True
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

# six.left=one
# six.right=three

y=Tree()
print(y.BalancedOfBinaryTree(five))