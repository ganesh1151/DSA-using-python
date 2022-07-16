def reverse(l,s,e):
    while s<e:
        l[s],l[e]=l[e],l[s]
        s+=1
        e-=1

def leftRoate(l,d):
    n=len(l)
    reverse(l,0,d-1)
    reverse(l,d,n-1)
    reverse(l,0,n-1)

l=[10,20,30,40,50,60]
d=3
print(l)
leftRoate(l,d)
print(l)