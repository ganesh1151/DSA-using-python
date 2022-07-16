class Node:
    def __init__(self,k):
        self.key=k
        self.next=None


def reverseList(head):
    stack=[]

    curr=head

    while curr is not None :
        stack.append(curr.key)
        curr=curr.next

    curr=head
    while curr is not None:
        curr.key=stack.pop()
        curr=curr.next

    return head

def printList(head):
    curr=head
    while curr!=None:
        print(curr.key,end=" ")
        curr=curr.next
    print()

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)

printList(head)

head=reverseList(head)

printList(head)