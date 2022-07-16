from collections import deque
l=[10,20,30,40,50]
d=2

dq=deque(l)
dq.rotate(-d)
l=list(dq)
print(l)
