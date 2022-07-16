def isPal(s):
    a=set()
    for i in s:
        if i in a:
            a.remove(i)
        else:
            if(i!="\n") or (i!=" "):
                a.add(i)
    if len(a)<=1:
        return True
    return False

s=input("Enter String: ")
print(isPal(s))