def rotate(l,d):
	l = l[d:] + l[:d]
	return l

def evenchar(str):
	i=1
	out=""
	for x in str:
		if i%2==0:
			if x in("a","i","o","e","u"):
				out=out+x
		i+=1
	return out

def output(list1,list2,m):
	if list1:
		print(-1)
	res=[len(str)]


	for i in len(list1):
		list1[i]=rotate(list1[i],list2[i])










m=int(input())

list1=[m]
list2=[m]

for i in range(len(m)):
		list1[i]=input()
		list2[i]=int(input())





