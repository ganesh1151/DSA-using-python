class Node:
    def __init__(self,k):
        self.left=None
        self.right=None
        self.key=k


def searchKey(root,key):
    if root is None:
        return False

    elif root.key==key:
        return True

    elif searchKey(root.left,key):
        return True

    else:
        return searchKey(root.right,key)

# Driver Code

root=Node(10)
root.left=Node(12)
root.right=Node(40)
root.right.left=Node(15)
root.right.right=Node(30)

print(searchKey(root,15))
print(searchKey(root,25))
print(searchKey(root,30))

