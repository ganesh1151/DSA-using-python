def countOccur(l,x):
    cnt=0

    for e in l:
        if e==x:
            cnt+=1

    return cnt

l=[10,20,20,20,30,30]

print(10,countOccur(l,10))
print(20,countOccur(l,20))
print(30,countOccur(l,30))
print(25,countOccur(l,25))