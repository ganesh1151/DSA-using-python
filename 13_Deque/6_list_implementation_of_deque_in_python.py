class MyDeque:
    def __init__(self,c):
        self.l=[None]*c
        self.cap=c
        self.size=0
        self.front=0

    def deleteFront(self):
        if self.size==0:
            return None
        else:
            res=self.l[self.front]
            self.front=(self.front+1)%self.cap
            self.size=self.size-1

            return res

    def insertFront(self,x):
        if self.size==self.cap:
            return
        else:
            self.front=(self.front-1)%self.cap
            self.l[self.front]=x
            self.size=self.size+1

    def insertRear(self,x):
        if self.size==self.cap:
            return
        new_rear=(self.front+self.size)%self.cap
        self.l[new_rear]=x
        self.size=self.size+1

    def deleteRear(self):
        sz=self.size
        if sz==0:
            return
        else:
            rear=(self.front+sz-1)%self.cap
            self.sizes=sz-1
            return self.l[rear]

    def frontEle(self):
        return self.l[self.front]

    def rearEle(self):
        rear=(self.front+self.size-1)%self.cap
        return self.l[rear]

dq=MyDeque(4)

dq.insertRear(10)
print(dq.frontEle(),dq.rearEle())
dq.insertFront(20)
print(dq.frontEle(),dq.rearEle())
dq.insertFront(30)
print(dq.frontEle(),dq.rearEle())
dq.deleteRear()
print(dq.frontEle(),dq.rearEle())
dq.insertRear(40)
print(dq.frontEle(),dq.rearEle())
dq.deleteRear()
print(dq.frontEle(),dq.rearEle())

