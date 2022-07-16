class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def delHead(head):
    if head==None:
        return None
    elif head.next==head:
        return None

    else:
        head.data=head.next.data
        head.next=head.next.next
        return head

def delKth(head,k):
    if head==None:
        return head

    elif k==1:
        return delHead(head)

    else:
        curr=head

        for i in range(k-2):
            curr=curr.next

        curr.next=curr.next.next
        return head

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
head.next.next=Node(15)
head.next.next.next=Node(30)
head.next.next.next.next=head

printCircular(head)

head=delKth(head,3)

printCircular(head)