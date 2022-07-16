def leftRoatate(l,d):
    for i in range(0,d):
        l.append(l.pop(i))

l=[10,20,30,40,50]
d=3
print(l)
leftRoatate(l,d)
print(l)