def parition(arr,p):
    n=len(arr)
    arr[p],arr[n-1]=arr[n-1], arr[p]

    temp=[]

    for x in arr:
        if x<=arr[n-1]:
            temp.append(x)

    for x in arr:
        if x>arr[n-1]:
            temp.append(x)

    for i in range(len(arr)):
        arr[i]=temp[i]

arr=[5,13,6,9,12,8,11]

parition(arr,5)

print(arr)
