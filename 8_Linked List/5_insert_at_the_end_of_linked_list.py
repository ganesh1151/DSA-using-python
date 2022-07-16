class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def insertEnd(head,key):
    temp = Node(key)
    if head==None:
        return temp

    curr=head
    while curr.next!=None:
        curr=curr.next

    curr.next=temp
    return head

head=None
head=insertEnd(head,10)
head=insertEnd(head,20)
head=insertEnd(head,30)

def printList(head):
    curr=head
    while curr!=None:
        print(curr.key,end=" ")
        curr=curr.next

printList(head)