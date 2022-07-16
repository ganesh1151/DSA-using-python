#using while loop
print("********* Using While Loop *********************")
s=input("Enter a string:\n")
low=0

high=len(s)-1

while low<high:
    if s[low]!=s[high]:
        print("No, Given string is not palindrom")
        break
    low+=1
    high-=1

else:
    print("yes, Given string is palindrome")

print()

#using slicing
print("************* Using Slicing **********************")

if s==s[::-1]:
    print("Yes, Given string is Palindrome")
else:
    print("No, Given string is not palindrome")

