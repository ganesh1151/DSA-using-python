def reverseList(l):
    s=0
    e=len(l)-1

    while s<e:
        l[s],l[e]=l[e],l[s]
        s+=1
        e-=1

l=[int(x) for x in input("Enter A number for a list").split(',')]
reverseList(l)
print(l)


"""
OUTPUT 

Enter A number for a list 10,20,30,40,50,60,70
[70, 60, 50, 40, 30, 20, 10]
"""