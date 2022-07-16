#ord and char
print(ord("a"))  #chr to ord   "unicode"
print(ord("A"))

print(chr(97))   # ord to chr    "unicode"
print(chr(65))
print()


#indexing

s="geek"
print(s)
print(s[0])
print(s[-1])
print(s[1])
print(s[-2])
print()


#multiline string
s="""Hi,
This is "python course"
Hope you are enjoying it."""
print(s)
print()



#string are immutable
s = "geek"
s[0] = "e"  # error: item assignment not supported
print(s)