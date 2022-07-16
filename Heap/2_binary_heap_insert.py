class myMinHeap:
    def __init__(self):
        self.arr=[]  # list to store values of heap items

    def parent(self,i):
        return (i-1)//2

    def lChild(self,i):
        return 2*i+1

    def rChild(self,i):
        return 2*i+2

    def insert(self,x):
        arr=self.arr
        arr.append(x)
        i=len(arr)-1

