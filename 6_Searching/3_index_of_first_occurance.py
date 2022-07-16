def firstIndex(l,x):
    for i in range(len(l)):
        if l[i]==x:
            return i

    return -1

l=[10,10,20,20,20,30,30,30,30,]
print(20,firstIndex(l,20))
print(30,firstIndex(l,30))
print(10,firstIndex(l,10))