class MyHash:
    def __init__(self,c):
        self.cap=c
        self.table=[-1]*c
        self.size=0

    def hash(self,x):
        return x%self.cap

    def search(self,x):
        h=self.hash(x)
        t=self.table
        i=h
        while t[i]!=-1:
            if t[i]==x:
                return True
            i=(i+1)%self.cap
            if i==h:
                return False
        return False

    def insert(self,x):
        if self.size==self.cap:
            return False

        if self.search(x)==True:
            return False

        i=self.hash(x)
        t=self.table
        while t[i] not in (-1,-2):
            i=(i+1)%self.cap

        t[i]=x
        self.size+=1
        return True

    def remove(self,x):
        h=self.hash(x)
        t=self.table
        i=h
        while t[i]!=-1:
            if t[i]==x:
                t[i]=-2
                return True
            i=(i+1)%self.cap
            if i==h:
                return False
        return False


h=MyHash(8)
h.insert(79)
h.insert(71)
h.insert(9)
h.insert(30)
h.insert(350)
print(h.search(9))
h.remove(9)
print(h.search(9))
