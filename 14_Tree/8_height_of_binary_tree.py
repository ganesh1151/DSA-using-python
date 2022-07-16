class Node:
    def __init__(self,k):
        self.left=None
        self.right=None
        self.key=k

def heightTree(root):
    if root==None:
        return 0

    else:
        lh=heightTree(root.left)
        rh=heightTree(root.right)
        return max(lh,rh)+1
        #return max(heightTree(root.left),heightTree(root.right))+1


#Driver Code

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)

print(heightTree(root))

