#Example 3:Delete Node in Binary Search tree  // Leet code 
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def DeleteInBinarySearchTree(root,key):
    if root is None:
        return None
    if root.val ==key:
        return Deletion(root)
    temp=root
    while temp is not None:
        if temp.val>key:
            if temp.left is not None and temp.left.val == key:
                temp.left=Deletion(temp.left)
                break
            else:
                temp=temp.left
        else:
            if temp.right is not None and temp.right.val==key:
                temp.right= Deletion(temp.right)
                break
            else:
                temp=temp.right
    return root

def Deletion(node):
    if node.left is None:
        return node.right
    if node.right is None:
        return node.left
    else:
        right_child=node.right
        last_right=findLastRight(node.left)
        last_right.right=right_child
        return node.left
def findLastRight(node):
    while node.right is not None:
        node=node.right
    return node
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


print(DeleteInBinarySearchTree(nine,3))