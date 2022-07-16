def rotateByone(l):
    n=len(l)
    x=l[0]

    for i in range(1,n):
        l[i-1]=l[i]

    l[n-1]=x

l=[10,20,30,40]
rotateByone(l)
print(l)