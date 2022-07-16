"""A set is an unordered collection of items. Every set element is unique
(no duplicates) and must be immutable (cannot be changed). However,
a set itself is mutable. We can add or remove items from it."""
#creation
print("************************ Creation *****************")

s1={10,20,30}
print(s1)

s2=set([20,30,40])
print(s2)

s3={}
print("expected type set ", type(s3))

s4=set()
print(type(s4))
print(s4)
print()


#insertion
print("******************** Insertion ********************")

s={10,20}
s.add(30)
print(s)

s.add(30)  # add duplicate item
print(s)

s.update([40,50])
print(s)

s.update([60,70],[80,90])  #insert multple list
print(s)
print()


#remove
print("******************** Remove *********************")
"""
The discard() method removes the specified item from the set. This method is different
 from the remove() method, because the remove() method will raise an error if the 
 specified item does not exist, and the discard() method will not
"""

s={10,30,20,40}
s.discard(30)
print(s)

s.remove(20)
print(s)

s.clear()
print(s)   #make set empty

s.add(50)
print(s)

del s  # delete the set

print()

#set operation on two set
#in operator is is faster in set than list because set uses hasing interll
print("********* set of operation on two set ***********")
s1={2,4,6,8}
s2={3,6,9}

print('union', s1 | s2)
print(s1.union(s2))

print('intersectoin',s1&s2)
print(s1.intersection(s2))

print("present in s1 but not present in s2", s1-s2)
print(s1.difference(s2))

print("symmetric difference, not present in both",s1^s2)
print(s1.symmetric_difference(s2))

print()

#set opeation on two sets
print("********** set operation on two set *************")
s1={2,4,6,8}
s2={4,8}
print("disjoint sets:",s1.isdisjoint(s2))

print("isSubset:",s1<=s2)
print(s1.issubset(s2))

print("proper set: ",s1<s2)

print("s1 is superset of s2:",s1>=s2)
print(s1.issuperset(s2))

print("s1 is proper superset of s2:",s1>s2)