def isSorted(l):
    i=1
    while i<len(l):
        if l[i]<l[i-1]:
            return  False
        i+=1

    return True

l=[int(x) for x in input("Enter Element for list: ").split(",")]

if isSorted(l):
    print("Yes, Given Element in sorted Order")
else:
    print("No, Given Element is not in sorted order")


