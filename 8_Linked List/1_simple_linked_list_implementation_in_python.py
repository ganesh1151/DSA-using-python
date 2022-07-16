class Node:
    def __init__(self,k):
        self.key=k
        self.next=None


temp1=Node(10)
temp2=Node(20)
temp3=Node(30)

temp1.next=temp2
temp2.next=temp3

head=temp1
print(head.key)
print(head.next.key)
print(head.next.next.key)