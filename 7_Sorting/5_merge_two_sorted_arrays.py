def merge(a,b):
    res=a+b
    res.sort()

    return res

a=[10,15,30]
b=[2,20]

print(*merge(a,b))