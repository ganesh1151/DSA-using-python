def getMax(l):
    for x in l:
        for y in l:
            if y>x:
                break
        else:          #if loop is existed naturally,no longer element found
            return x
    return  None   # this excute when list is empty


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




x, y = [int(x) for x in input("Enter two values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)