class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def insertPos(head,data,pos):
    temp=Node(data)
    if pos==1:
        temp.next=head
        return temp

    curr=head
    for i in range(pos-2):
        curr=curr.next
        if curr==None:
            return head
    temp.next=curr.next
    curr.next=temp

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
head.next.next.next.next=Node(50)

printList(head)

head=insertPos(head,45,4)

printList(head)