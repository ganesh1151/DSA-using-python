def getSmaller(l,n):
    res=[]

    for x in l:
        if x<n:
            res.append(x)

    return  res

l=[10,60,80,12,30,80,99,41,2]
n=50
print(getSmaller(l,n))
