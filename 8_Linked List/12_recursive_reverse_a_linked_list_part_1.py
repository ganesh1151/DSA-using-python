class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def reverseList(head):
    if head==None:
        return head
    if head.next==None:
        return head

    rest_head=reverseList(head.next)
    rest_tail=head.next
    rest_tail.next=head
    head.next=None

    return rest_head

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

