#Height of binary tree Leet code 104
from collections import deque
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
#Solution Using reursion
def HeightOfBinaryTree(node):
    if node==None:
        return 0
    leftSide=HeightOfBinaryTree(node.left)
    rightSide=HeightOfBinaryTree(node.right)
    return 1+max(leftSide,rightSide)
def HeightOfBinaryTrees(node):
    queue=deque([])
    height=0
    queue.append(node)
    while len(queue)!=0:
        level=len(queue)
        height+=1
        for i in range(level):
            e=queue.popleft()
            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)
    return height
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

x=HeightOfBinaryTree(five)
print(x)

y=HeightOfBinaryTrees(five)
print(y)