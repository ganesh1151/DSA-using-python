class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def printCircular(head):
    if head==None:
        return
    print(head.key,end=" ")
    curr=head.next
    while curr!=head:
        print(curr.key,end=" ")
        curr=curr.next

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=head

printCircular(head)