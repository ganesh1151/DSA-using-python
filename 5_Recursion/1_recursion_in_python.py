#background
def fun1():
    print("fun1 called")

def fun2():
    print("Before fun1()")
    fun1()
    print("After fun1()")


print("Before fun2()")
fun2()
print("After fun2()")

print()

#direct recursive program1
def fun3():
    print("GFG")
    fun()


#direct recursive program 2
print("************* program 2 *****************")
def fun(n):
    if n==0:
        return
    print("GFG")
    fun(n-1)

fun(3)


