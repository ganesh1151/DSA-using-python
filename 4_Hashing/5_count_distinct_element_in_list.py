
def cDistinct(l):
    res=1

    for i in range(1,len(l)):
        if l[i] not in l[0:i]:
            res=res+1

    return res

l=[10,20,10,30,30,20]

print(cDistinct(l))


print("***************************")

def cDistinct2(l):
    return len(set(l))

print(cDistinct2(l))