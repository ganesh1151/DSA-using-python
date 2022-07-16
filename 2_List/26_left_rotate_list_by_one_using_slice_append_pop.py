
l=[10,20,30,40]
print(l)
l=l[1:]+l[0:1]
print(l)

l=[10,20,30,40]
print(l)
l.append(l.pop(0))
print(l)