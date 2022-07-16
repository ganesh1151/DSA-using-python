from _collections import deque
d=deque([10,20,30,40,50])
d.rotate(2)  # right roatation (positive)
print(d)
d.rotate(-2)  #left roataion (negative)
print(d)
d.reverse()
print(d)