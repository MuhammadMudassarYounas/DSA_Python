#Example 3:Morris Algorithm in Binary Search tree  // Leet code 
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
#inOrder Traversal
def MorrisAlgorithmInBinarySearchTree(root):
    result=[]
    current=root
    while current is not None:
        if current.left is None:
            result.append(current.val)
            current=current.right
        else:
            p=current.left
            while (p.right is not None and p.right !=current):
                p=p.right
            if p.right is None:
                p.right=current
                current=current.left
            else:
                p.right=None
                result.append(current.val)
                current=current.right
    return result
#preOrder Traversal
    def MorrisAlgorithmInBinarySearchTree(root):
    result=[]
    current=root
    while current is not None:
        if current.left is None:
            result.append(current.val)
            current=current.right
        else:
            p=current.left
            while (p.right is not None and p.right !=current):
                p=p.right
            if p.right is None:
                result.append(current.val)
                p.right=current
                current=current.left
            else:
                p.right=None
                current=current.right
    return result
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


print(MorrisAlgorithmInBinarySearchTree(nine))