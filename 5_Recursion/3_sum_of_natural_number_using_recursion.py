#problem 1
print("************ Sum of natural number ***********")
def sumOfNatural(n):
    if n==0:
        return 0
    else:
        return n+sumOfNatural(n-1)

n=int(input("Enter no : "))
print(sumOfNatural(n))
print()


#problem 2
print("*********** print number from n to 1 **************")
def printNumber(n):
    if n==0:
        return
    print(n)
    printNumber(n-1)

printNumber(n)
print()

#problem 3
print("*************** print number from 1 to n *********")
def printNo1toN(n):
    if n==0:
        return
    printNo1toN(n-1)
    print(n)

printNo1toN(n)
print()