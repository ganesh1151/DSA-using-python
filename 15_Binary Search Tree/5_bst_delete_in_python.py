class Node:
    def __init__(self,key):
        self.left=None
        self.key=key
        self.right=None


def getSucc(curr,key):
    while curr.left!=None:
        curr=curr.left

    return curr.key

def deleteNode(root,key):
    if root==None:
        return

    if root.key>key:
        root.left=deleteNode(root.left,key)

    if root.key<key:
        root.right=deleteNode(root.right,key)

    else:
        if root.left==None:
            return root.right
        elif root.right==None:
            return root.left

        else:
            succ=getSucc(root.right,key)
            root.key=succ
            root.right=deleteNode(root.right,succ)

    return root