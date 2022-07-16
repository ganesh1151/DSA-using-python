class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

def deleteLast(head):
    if head==None or head.next==None:
        return None

    curr = head
    while curr.next.next != None:
        curr = curr.next

    curr.next = None
    return head

def printDll(head):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next

    print()

head=Node(10)
temp1=Node(20)
temp2=Node(30)

head.next=temp1
temp1.prev=head

temp1.next=temp2
temp2.prev=temp1

printDll(head)

head=deleteLast(head)

printDll(head)
