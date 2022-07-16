
#3 formated
name="ABC"
course="Python Course"

s="Welcome %s to the %s"%(name,course)
print(s)
print()

# using format function
s="Welcome {0} to the {1}".format(name,course)
print(s)
print()

#using f-string
s=f"welcome{name} to the {course}"
print(s)
print()


print("###################################")

# f-string
a=10
b=20

print(f"sum of {a} and {b} is {a+b}")
print(f"product of {a} and {b} is {a*b}")


print("###################################")
s1="ABC"
s2="abc"

print(f"lower case of {s1} is {s1.lower()}")
print(f"upper case of {s2} is {s2.upper()}")