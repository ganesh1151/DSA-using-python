from _collections import deque
stack=deque()

stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
print(stack.pop())

top=stack[-1]
print(top)
size=len(stack)
print(size)
