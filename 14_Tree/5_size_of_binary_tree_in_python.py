class Node:
    def __init__(self,k):
        self.left=None
        self.right=None
        self.key=k

def treeSize(root):
    if root==None:
        return 0
    else:
        ls=treeSize(root.left)     #we can also use
        rs=treeSize(root.right)    #return treeSize(root.left)+treeSize(root.right) +1
        return ls+rs+1

#driver Code

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)

print(treeSize(root))
