#Example 9:Lowest common ancestor in Binary Search tree  // Leet code 
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def LowestCommonAncestor(root,p,q):
    def solve(node,p,q):
        if node is None:
            return None
        if node== p or node == q:
            return node
        left=solve(node.left,p,q)
        right=solve(node.right,p,q)
        if left is None and right is None:
            return None
        elif left is None: 
            return right
        elif right is None:
            return left
        return node
    return solve(root,p,q)

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

print(LowestCommonAncestor(nine,two,eight))