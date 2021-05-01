# 요세푸스 문제
from collections import deque

N, K = map(int,input().split())
queue = deque([idx+1 for idx in range(N)])
answer = []

while(len(queue) != 0):
    for _ in range(K-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

# print(answer)
print("<{}>" .format(", ".join(map(str,answer))))