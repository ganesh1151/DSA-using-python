class MyHash:
    def __init__(self,b):
        self.BUCKET=b
        self.table=[[] for x in range(b)]

    def insert(self,x):
        i=x%self.BUCKET
        self.table[i].append(x)

    def remove(self,x):
        i=x%self.BUCKET
        if x in self.table[i]:
            self.table[i].remove(x)

    def search(self,x):
        i=x%self.BUCKET
        return x in self.table[i]

h=MyHash(8)
h.insert(79)
h.insert(71)
h.insert(9)
h.insert(30)
h.insert(350)
print(h.search(9))
h.remove(9)
print(h.search(9))


