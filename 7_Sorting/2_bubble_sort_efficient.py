def bubbleSort(l):

    n=len(l)

    for i in range(n-1):
        swapped=False

        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]

                swapped=True

        if swapped==False:
            return

l=[10,8,20,5]

bubbleSort(l)

print(*l)