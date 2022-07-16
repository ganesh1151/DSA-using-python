def getEvenOdd(l):
    even=[]
    odd=[]

    for x in l:
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)

    return even,odd

l=[10,15,26,31,40,50,60,87,97]
even, odd=getEvenOdd(l)

print("even value are ", even,)
print("odd value are ", odd)