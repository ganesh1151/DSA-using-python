class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def inserEnd(head,x):
    temp=Node(x)

    if head==None:
        temp.next=temp
        return temp
    else:
        temp.next=head.next
        head.next=temp

        temp.data,head.data=head.data,temp.data   #swapping data
        return temp


def printCircular(head):
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
head.next.next=head

printCircular(head)

head=inserEnd(head,30)

printCircular(head)