
def getMax(l):
    if not l:
        return  None
    else:

        res=l[0]
        for i in range(1,len(l)):
            if l[i]>res:
                res=l[i]
        return res


"""The developer often wants a user to enter multiple values or inputs in one line. 
In C++/C user can take multiple inputs in one line using scanf but in Python user can
 take multiple values or inputs in one line by two methods. 

Using split() method
Using List comprehension
This function helps in getting multiple inputs from users. It breaks the given input 
by the specified separator. If a separator is not provided then any white space is a separator. 
Generally, users use a split() method to split a Python string but one can use it in 
taking multiple inputs."""



l = [int(x) for x in input().split()]
print(getMax(l))
print(l)

"""
OUTPUT
10 20 30 40 60 80 70 90
90
[10, 20, 30, 40, 60, 80, 70, 90]
"""