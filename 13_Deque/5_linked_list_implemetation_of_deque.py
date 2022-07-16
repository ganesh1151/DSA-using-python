class Node:
    def __init__(self,k):
        self.key=k
        self.next=None
        self.prev=None

class MyDeque:
    def __init__(self,c):
        self.front=None
        self.rear=None
        self.sz=0

    def size(self):
        return self.sz

    def isEmpty(self):
        return self.sz==0

    def inserRear(self,x):
        temp=Node(x)
        if self.rear==None:
            self.front=temp
        else:
            self.rear.next=temp
            temp.prev=self.rear
        self.rear=temp
        self.sz=self.sz+1

    def deletefront(self):
        if self.front==None:
            return None
        else:
            res=self.front.key
            self.front=self.front.next
            if self.front==None:
                self.rear=None

            else:
                self.front.prev=None
            self.sz=self.sz-1

            return res

    def getFront(self):
        if self.front:
            return self.front.key

    def getRear(self):
        if self.rear:
            return self.rear.key

#main
dq=MyDeque(3)

print(dq.isEmpty())
dq.inserRear(10)
print(dq.getFront(),dq.getRear())
dq.inserRear(20)
print(dq.getFront(),dq.getRear())
dq.inserRear(30)
print(dq.getFront(),dq.getRear())
dq.deletefront()
print(dq.getFront(),dq.getRear())

