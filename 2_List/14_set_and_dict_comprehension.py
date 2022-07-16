l={10,20,3,4,10,20,7,3}

s1={x for x in l if x%2==0}
s2={x for x in l if x%2!=0}
print(s1)
print(s2)

l1=[1,3,4,2,5]

d1={x:x**3 for x in l1}
print(d1)

"""The f means Formatted string literals and it's new in Python 3.6 . A formatted string literal
 or f-string is a string literal that is prefixed with 'f' or 'F' . These strings may contain 
 replacement fields, which are expressions delimited by curly braces {}"""
d2={x:f"ID{x}" for x in range(5)}
print(d2)

#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "ganesh", age = 20)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("ganesh",20)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("ganesh",20)
print(txt1)
print(txt2)
print(txt3)


l2=[101.103,102]
l3=["gfg","ide","course"]

d3={l2[i]:l3[i] for i in range(len(l2))}
print(d3)

"""To create a dictionary from two sequences, use the dict() and zip() method.
 In Python 3, the zip() method now returns a lazy iterator, which is now the most used approach. 
 The dict(zip(keys, values)) need the one-time global lookup each for dict and zip."""
d4=dict(zip(l2,l3))
print(d4)
