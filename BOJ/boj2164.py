from collections import deque

N = int(input())
queue = [ idx+1 for idx in range(N) ]
queue = deque(queue)

while(len(queue) > 1):
    queue.popleft()
    if len(queue) == 1:
        break
    queue.append(queue.popleft())

print(queue.popleft())