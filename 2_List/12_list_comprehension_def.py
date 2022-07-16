def getEevenOdd(l):
    even=[x for x in l if x%2==0]
    odd=[x for x in l if x%2!=0]
    return  even, odd

l=[10,20,23,54,57,32,14,21,51]

even,odd=getEevenOdd(l)
print("even number are",even)
print("odd number are",odd)


"""
OUTPUT
even number are [10, 20, 54, 32, 14]
odd number are [23, 57, 21, 51]
"""