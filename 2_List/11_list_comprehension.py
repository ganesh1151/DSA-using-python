l1=[x for x in range(11) if x%2==0]
print(l1)

l2=[x for x in range(11) if x%2!=0]
print(l2)

#code for smaller
def getsmaller(l,n):
    return [e for e in l if e<n]

l=[1,30,20,2,7,8,45,54]
n=22

print(getsmaller(l,n))


"""
OUTPUT
[0, 2, 4, 6, 8, 10]
[1, 3, 5, 7, 9]
[1, 20, 2, 7, 8]
"""