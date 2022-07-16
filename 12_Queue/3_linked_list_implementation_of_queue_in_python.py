class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

class MyQueue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.sz=0

    def size(self):
        return self.sz

    def isEmpty(self):
        return self.sz==0

    def getFront(self):
        return self.front.key

    def getRear(self):
        return self.rear.key

    def enque(self,x):
        temp=Node(x)
        if self.rear==None:
            self.front=temp
        else:
            self.rear.next=temp

        self.rear=temp
        self.sz=self.sz+1

    def deque(self):
        if self.front==None:
            return None
        else:
            res=self.front.key
            self.front=self.front.next
            if self.front==None:
                self.rear=None
            self.sz=self.sz-1
            return res

q=MyQueue()
q.enque(10)
print(q.getFront(),q.getRear())
q.enque(20)
print(q.getFront(),q.getRear())
q.enque(30)
print(q.getFront(),q.getRear())
q.deque()
print(q.getFront(),q.getRear())
