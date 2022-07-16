def bSearch(l,x):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2

        if l[mid]==x:
            return mid
        elif(l[mid]<x):
            low=mid+1
        else:
            high=mid-1
    return -1


l=[10,20,30,40,50,60]

print(30,bSearch(l,30))
print(20,bSearch(l,20))
print(10,bSearch(l,10))
print(60,bSearch(l,60))
print(40,bSearch(l,40))
print(55,bSearch(l,55))
print(-50,bSearch(l,-50))