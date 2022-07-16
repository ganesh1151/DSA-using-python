from math import inf

class Node:
    def __init__(self,k):
        self.left=None
        self.right=None
        self.key=k


def getMax(root):
    if root==None:
        return -inf
    else:
        lm=getMax(root.left)
        rm=getMax(root.right)
        return max(root.key,lm,rm)
        # return max(root.key, getMax(root.left), getMax(root.right))


#driver Code

root=Node(10)
root.left=Node(80)
root.right=Node(15)
root.right.left=Node(40)
root.right.right=Node(50)

print(getMax(root))