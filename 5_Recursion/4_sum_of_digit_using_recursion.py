def sumOfDigit(n):
    if n==0:
        return 0
    return n%10+sumOfDigit(n//10)

n=int(input("Enter No : "))
print(sumOfDigit(n))
