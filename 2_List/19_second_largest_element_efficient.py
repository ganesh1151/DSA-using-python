def getSecMax(l):
    if len(l)<=1:
        return None
    lar=l[0]; slar=None

    for x in l[1:]:
        if x> lar:
            slar=lar
            lar=x
        elif x!=lar:
            if slar==None or slar<x:
                slar=x
    return  slar

l=[int(x) for x in input("Enter element in list: ").split()]
print(getSecMax(l))

"""
OUTPUT 
Enter element in list: 10 20 6 50 88 4 6 
50
"""