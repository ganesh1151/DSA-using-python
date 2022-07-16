
#checking for substring
s1="geeksforgeeks"
s2="geeks"

print(s2 in s1)
print( s2 not in s1)

#concatenation
s1="geeks"
s2="for"
s3=s1+s2

s4="welcome to "+ s1 + s2

print(s3)
print(s4)


#Position of Substring
s1="geeksforgeeks"
s2="geek"

print(s1.index(s2))
print(s1.rindex(s2))  #right index
print(s1.index(s2,0,13))  #start and end index

