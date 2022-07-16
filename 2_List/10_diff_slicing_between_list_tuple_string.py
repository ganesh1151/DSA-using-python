l1=[10,20,30]
l2=l1[:]

t1=(10,20,30)
t2=t1[:]

s1="ganesh"
s2=s1[:]

print("list having same element but doesn't have same id->",l1 is l2)
print("tuple having same elment has same id->", t1 is t2)
print("string of same value have same id->",s1 is s2)

