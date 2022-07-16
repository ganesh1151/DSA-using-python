from _collections import deque

q=deque()
q.append(10)
q.append(20)
q.append(30)
print(q)
print(q.popleft())
q.append(40)
print(q.popleft())
print(len(q))
print(q[0])
print(q[-1])

