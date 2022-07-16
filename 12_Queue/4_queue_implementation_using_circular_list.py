class MyQueue:
    def __init__(self,c):
        self.l=[None]*c
        self.cap=c
        self.size=0
        self.front=0

    def getFront(self):
        if self.size==0:
            return None
        else:
            return self.l[self.front]

    def getRear(self):
        if self.size==0:
            return None
        else:
            rear=(self.front+self.size-1)%self.cap
            return self.l[rear]

    def enque(self,x):
        if self.size==self.cap:
            return

        else:
            rear=(self.front+self.size-1)%self.cap
            rear=(rear+1)%self.cap
            self.l[rear]=x

            self.size=self.size+1
    def deque(self):
        if self.size==0:
            return None
        else:
            res=self.l[self.front]
            self.front=(self.front+1)%self.cap
            self.size=self.size-1

            return res

# Main
q=MyQueue(4)
q.enque(10)
print(q.getFront(),q.getRear())
q.enque(20)
print(q.getFront(),q.getRear())
q.enque(30)
print(q.getFront(),q.getRear())
q.enque(40)
print(q.getFront(),q.getRear())
q.deque()
print(q.getFront(),q.getRear())
q.deque()
print(q.getFront(),q.getRear())
q.enque(50)
print(q.getFront(),q.getRear())

