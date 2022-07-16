s="geekforgeeks"
l1=[x for x in s if x in "aeiou"]
print(l1)

l2=["geeks","ide","courses","gfg"]
l3=[x for x in l2 if x.startswith("g")]
print(l3)

l4=[x*2 for x in range(6)]
print(l4)


print("-------------------------")
l1=["geeks","fear","geeks","gfg","ide"]
l2=[x.upper() for x in l1 if x.startswith("g")]
print(l2)