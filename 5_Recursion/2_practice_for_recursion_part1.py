#problem 1
print("*************** Problem 1 ***********************")
def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
    print(n)

fun(3)

#problem 2
print("***************** Problem 2 ***********************")
def fun1(n):
    if n==0:
        return
    fun1(n-1)
    print(n)
    fun1(n-1)

fun(3)

#problem 3
print("****************** Problem 3 **********************")
def fun2(n):
    if n<=1:
        return 0
    else:
        return 1+fun2(n/2)

print(fun2(16))
print()


#problem 4
print("*************** Problem 4 *************************")
def fun3(n):
    if n==0:
        return
    fun3(n//2)
    print(n%2)

fun3(13)