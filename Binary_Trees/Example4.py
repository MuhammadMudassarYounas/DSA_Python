#Binary Tree maximum path sum leet code 124  
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Tree:
    def MaximumSumBinaryTree(self,node):
        self.maxiSum=float("-inf")
        def solve(root):
            if root == None:
                return 0
            LS=solve(root.left)
            RS=solve(root.right)
            self.maxiSum=max(self.maxiSum,LS+root.val+RS)
            return root.val+max(LS,RS)
        solve(node)
        return self.maxiSum
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
print(y.MaximumSumBinaryTree(five))