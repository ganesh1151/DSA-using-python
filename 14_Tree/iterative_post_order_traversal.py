# Simple Python3 program to print
# PostOrder Traversal(Iterative)

# A binary tree node
class Node:

    def __init__(self, x):
        self.data = x
        self.right = None
        self.left = None


# Create a postorder class

# An iterative function to do postorder
# traversal of a given binary tree
def postOrderIterative(root):
    stack = []

    while (True):
        while (root != None):
            stack.append(root)
            stack.append(root)
            root = root.left

        # Check for empty stack
        if (len(stack) == 0):
            return

        root = stack.pop()

        if (len(stack) > 0 and stack[-1] == root):
            root = root.right
        else:
            print(root.data, end=" ")
            root = None


# Driver code
if __name__ == '__main__':
    # Let us create trees shown
    # in above diagram
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Post order traversal of binary tree is :")

    postOrderIterative(root)

# This code is contributed by mohit kumar 29
