class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

def prindll(head):
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

prindll(head)
