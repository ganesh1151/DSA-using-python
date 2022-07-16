class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def deleteHead(head):
    if head==None:
        return None
    elif head==head.next:
        return None

    curr=head
    while curr.next!=head:
        curr=curr.next
    curr.next=head.next
    return curr.next

def printCicular(head):
    if head==None:
        return
    print(head.data,end=" ")
    curr=head.next
    while curr!=head:
        print(curr.data,end=" ")
        curr=curr.next

    print()

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=head

printCicular(head)

head=deleteHead(head)

printCicular(head)