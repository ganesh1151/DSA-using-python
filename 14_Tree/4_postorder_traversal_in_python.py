class Node:
    def __init__(self,k):
        self.left=None
        self.right=None
        self.key=k

def postorder(root):
    if root !=None:
        postorder(root.left)
        postorder(root.right)
        print(root.key)

#driver code
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)

postorder(root)
