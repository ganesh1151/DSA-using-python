txt=input("Enter Text:\n")
pat=input("Enter Pattern:\n")

pos=txt.find(pat)

while pos>=0:
    print(pos)
    pos=txt.find(pat,pos+1)


"""
OUTPUT

Enter Text:
geeks for geeks
Enter Pattern:
geeks
0
10
"""