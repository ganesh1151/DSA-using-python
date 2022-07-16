#naive solution

def isAnagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    s1=sorted(s1)
    s2=sorted(s2)
    return (s1==s2)

s1="listen"
s2="silent"
print(isAnagram(s1,s2))


#efficient solution
print("**************** Efficient solution **************")
def isAnagram(s1,s2):
    if len(s1)!=len(s2):
        return False

    count=[0]*256
    for i in range(len(s1)):
        count[ord(s1[i])]+=1
        count[ord(s2[i])]-=1

    for x in count:
        if x!=0:
            return False
    return True


print(isAnagram(s1,s2))
