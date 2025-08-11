from collections import deque

list = deque([])
list.append(100)
list.append(200)
list.append(300)
list.appendleft(10)
list.appendleft(50)

print(list)
list.popleft()
print(list)