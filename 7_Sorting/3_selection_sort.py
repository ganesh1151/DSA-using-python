def selectSort(l):
    n=len(l)

    for i in range(n-1):
        mid_ind=i
        for j in range(i+1,n):
            if l[j]<l[mid_ind]:
                mid_ind=j

        l[mid_ind],l[i]=l[i],l[mid_ind]

l=[10,5,8,20,2,18]

selectSort(l)

print(*l)

