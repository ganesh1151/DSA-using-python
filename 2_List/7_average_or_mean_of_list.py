def average(l):
    sum=0
    for i in l:
        sum+=i
    n=len(l)
    return sum/n


l=[10,15,30,20,25]
print(average(l))


#using build in function
def averagge(l):
    return sum(l)/len(l)

print(average(l))