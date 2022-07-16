#ceiling means closer to greater or equal value
class Node:
    def __init__(self,key):
        self.left=None
        self.key=key
        self.right=None


def getCeil(root,x):
    res=None
    while root!=None:
        if root.key==x:
            return root

        elif root.key<x:
            root=root.right

        else:
            res=root
            root=root.left

    return res

