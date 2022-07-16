l=[10,20,30,40,50]

#for appending element at last
l.append(100)
print(l)

#for insert element at specific position
l.insert(2,130)
print(l)

#for checking element is present in list or not
print(15 in l)
print( 100 in l)

#for count of specific element in list
print(l.count(100))
l.insert(3,100)
print(l.count(100))


#for finding first index of element if its is not present then it will show an error
print(l.index(100))