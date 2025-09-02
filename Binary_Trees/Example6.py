#Bottom View in Binary tree geek for geek
from collections import deque  
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Tree:
    def bottomViewOfBinaryTree(self,node):
        if node == None:
            return
        result=[]
        Dictionary={}
        queue=deque()
        queue.append((node,0))
        while queue:
            e,line=queue.popleft()
            # if line not in Dictionary:
            Dictionary[line]=e.val
            # if line in Dictionary:
            #     Dictionary[line]=e.val
            if e.left:
                queue.append((e.left,line-1))
            if e.right:
                queue.append((e.right,line+1))
        for value in sorted(Dictionary.items()):
            result.append(value[1])
        return result
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
print(y.bottomViewOfBinaryTree(five))