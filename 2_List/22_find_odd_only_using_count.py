def findodd(l):
    res=None
    for x in l:
        count=l.count(x)

        if count%2!=0:
            res=x
            break
    return res

l=[int(x) for x in input("Enter element for list: ").split()]
print(findodd(l))

"""
OUTPUT 
Enter element for list: 10 20 30 30 20 10
None


OUTPUT :
Enter element for list: 10 20 30 20 10
30
"""