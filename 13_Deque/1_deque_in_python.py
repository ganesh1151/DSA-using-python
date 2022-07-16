print("**************** Using deque **********")
from _collections import deque
d=deque()
d.append(10)
d.append(20)
d.append(30)
d.appendleft(40)
print(d)
print(d.pop())
print(d.popleft())
print(d)
print()

print("*************** Using a List ***********")
from _collections import deque
d=deque([10,20,30,40])
d.insert(2,10)
print(d.count(10))
d.remove(10)
d.extend([50,60])
print(d)
d.extendleft([15,25])
print(d)
print()


