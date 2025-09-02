#Right View in Binary tree Leet code 199
from collections import deque  
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Tree:
    def RightViewOfBinaryTree(self,root):
        if root == None:
            return
        result=[]
        queue=deque()
        queue.append(root)
        while len(queue)!=0:
            level=len(queue)
            for i in range(level):
                e=queue.popleft()
                if i==level-1:
                    result.append(e.val)
                if e.left is not None:
                    queue.append(e.left)
                if e.right is not None:
                    queue.append(e.right)

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
print(y.RightViewOfBinaryTree(five))