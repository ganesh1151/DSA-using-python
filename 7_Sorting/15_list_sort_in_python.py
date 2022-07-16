#Program 1
print("****************** list ********************")
l1=[5,10,15,1]
l1.sort()
print(l1)

l2=[1,5,3,10]
l2.sort(reverse=True)
print(l2)

l3=['gfg','die','courses']
l3.sort()
print(l3)

def myFun(s):
    return len(s)

l=['gfg','courses','python']
l.sort(key=myFun)
print(l)

l.sort(key=myFun,reverse=True)
print(l)

#Program 2
print("*********** sorting user defined using key-fun **********")
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

def myFun(p):
    return p.x

l=[Point(1,15),Point(10,5),Point(3,8)]
l.sort(key=myFun)

for i in l:
    print(i.x,i.y)


#Program 3
print("********** Sorting user Defined using __lt__1 **********")
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __lt__(self, other):
        return self.x<other.x

l=[Point(1,15),Point(10,5),Point(5,8)]

for i in l:
    print(i.x,i.y)

print("****** sorting user defined using __lt__2 **************")

class Point2:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __lt__(self, other):
        if self.x==other.x:
            return self.y<other.y
        else:
            return self.x<other.x

l=[Point2(1,15), Point2(10,5), Point2(1,8)]
l.sort()

for i in l:
    print(i.x,i.y)


