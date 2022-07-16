class Node:
    def __init__(self, key):
        self.left = None
        self.key = key
        self.right = None

def insert(root,key):
    if root==None:
        return Node(key)
    elif root.key==key:
        return root
    elif root.left>key:
        root.left=insert(root.left,key)
    else:
        root.right=insert(root.right,key)
    return root


