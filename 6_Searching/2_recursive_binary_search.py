def bSearch(l,x,low,high):
    if low>high:
        return -1

    mid=(low+high)//2
    if l[mid]==x:
        return mid

    elif l[mid]>x:
        return bSearch(l,x,low,mid-1)

    else:
        return bSearch(l,x,mid+1,high)

def bSearchMain(l,x):
    return bSearch(l,x,0,len(l)-1)

l=[10,20,30,40,50,60]

print(30,bSearchMain(l,30))
print(20,bSearchMain(l,20))
print(10,bSearchMain(l,10))
print(60,bSearchMain(l,60))
print(40, bSearchMain(l, 40))
print(55, bSearchMain(l, 55))
print(-50, bSearchMain(l, -50))