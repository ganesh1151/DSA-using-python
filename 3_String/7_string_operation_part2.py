
#len, lower and upper
print("************ Len, lower and upper ************** ")
s1="geeks"

print(len(s1))

s2=s1.upper()

print(s2)

s3=s2.lower()
print(s3)

print(s1.islower())
print(s2.isupper())
print()


#startwith and endwith function
print("******** startwith and endwith function ***********")
s="GeeksforGeeks Python Course"

print(s.startswith("Geeks"))
print(s.endswith("Course"))
print(s.startswith("Geeks",1))  #start index
print(s.startswith("Geeks",8,len(s)))  #start index, last index
print()

#split and join
#split function convert string into list and viceversa
print("********* split and join funciton ****************")
s1="geeks for geeks"
print(s1.split())      #split by space

s2="geeks, for, geeks"
print(s2.split(','))   #split by comma

l=["geeksforgeeks","python","course"]
print(" ".join(l))      #join by space
print(",".join(l))      #join by comma


#strip function remove the unwanted character from the sting
print("************* strip ***********************")
s1="__geeksforgeeks__"
print(s1.strip("_"))   #strip from both side
print(s1.lstrip("_"))    #strip from left side
print(s1.rstrip("_"))  #strip from right side
print()


#find function if given string is not found then it will return -1
print("****************** find function ****************")
s1="geeks for geeks"
s2="geeks"
print(s1.find((s2)))
print(s1.find("gfg"))
n=len(s1)
print(s1.find(s2,1,n))