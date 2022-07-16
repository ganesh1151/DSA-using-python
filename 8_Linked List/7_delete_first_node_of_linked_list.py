class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def delFirst(head):
    if head==None:
        return None
    else:
        return head.next

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

head=delFirst(head)

printList(head)