def findOdd(l):
    res=0

    for x in l:
        res=res^x

    return res

l=[int(x) for x in input("Enter Elemenet for list: ").split(",")]
print(findOdd(l))

"""
OUTPUT 
Enter Elemenet for list: 10,20,30,10,20
30
"""