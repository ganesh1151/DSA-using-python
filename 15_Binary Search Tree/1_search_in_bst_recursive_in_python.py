def searchBst(root,key):
    if root is None:
        return False

    elif root.key==key:
        return True

    elif root.left>key:
        return searchBst(root.left,key)
    else:
        return searchBst(root.right,key)

