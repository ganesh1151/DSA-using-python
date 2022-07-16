class Node:
    def __init__(self,k):
        self.key=k
        self.left=None
        self.right=None


def inorder(root):
    if root !=None:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)

# drive code
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)

inorder(root)
