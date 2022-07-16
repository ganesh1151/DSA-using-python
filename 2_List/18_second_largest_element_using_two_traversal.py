"""None is used to define a null value. It is not the same as an empty string,
False, or a zero. It is a data type of the class NoneType object. Assigning a value of
 None to a variable is one way to reset it to its original, empty state"""
def getMax(l):

    if not l:
        return None

    else:
        res = l[0]
        for i in range(1,len(l)):
            if l[i]>res:
                res=l[i]
        return res


def getSecMax(l):
    if len(l)<=1:
        return None

    lar=getMax(l)
    slar=None

    for x in l:
        if x!=lar:
            if slar==None:
                slar=x
            else:
                slar=max(slar,x)
    return  slar

l=[int(x) for x in input().split()]
print(getSecMax(l))

"""
OUTPUT 
10 20 50 3 60 80 40 
60
"""