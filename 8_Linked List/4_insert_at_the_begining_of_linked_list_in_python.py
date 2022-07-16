class Node:
    def __init__(self,k):
        self.key=k
        self.next=Node

def insertBegin(head,key):
    temp=Node(key)
    temp.next=head
    return temp

head=None
head=insertBegin(head,10)
head=insertBegin(head,20)
head=insertBegin(head,30)

def printList(head):
    curr=head
    while curr!=None:
        print(curr.key,end=" ")
        curr=curr.next

printList(head)