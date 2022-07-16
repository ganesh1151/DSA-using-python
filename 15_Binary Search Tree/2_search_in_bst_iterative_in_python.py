def searchBst(root,key):
    while root is not None:

        if root.key==key:
            return True
        elif root.left>key:
            root=root.left
        else:
            root=root.right
    return False
