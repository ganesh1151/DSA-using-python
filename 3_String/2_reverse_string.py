#string in python are immutable

#using loop
s=input("Enter a string: ")
rev=""
for i in s:
    rev=i+rev
print("reverse string is: ",rev)
print()


#using slicing
s=input("Enter a String: ")
print(s[::-1])

"""
OUTPUT
Enter a string: ganesh
reverse string is:  hsenag

Enter a String: ganesh
hsenag
"""