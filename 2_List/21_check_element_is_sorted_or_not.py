def isSorted(l):
    l2=sorted(l)  # build in function for sorting list

    if l==l2:
        return True
    else:
        return False

l=[int(x) for x in input("Enter Element for list: ").split()]

if isSorted(l):
    print("Yes, Given Element is in Sorted Order")
else:
    print("No, Given Element is not in Sorted Order")


"""
OUTPUT
1)Enter Element for list: 10 20 30 40 50 60 
Yes, Given Element is in Sorted Order

2)Enter Element for list: 10 20 30 60 50 40
No, Given Element is not in Sorted Order
"""