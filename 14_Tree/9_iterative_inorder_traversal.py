class Node:
    def __init__(self,k):
        self.left=None
        self.right=None
        self.key=k


def itrInorder(root):
    if root is None:
        return

    st=[]
    curr=root
    while curr is not None:
        st.append(curr)
        curr=curr.left

    while len(st)>0:
        curr=st.pop()
        print(curr.key)
        curr=curr.right

        while curr is not None:
            st.append(curr)
            curr=curr.left


#Driver Code

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)

itrInorder(root)