'''
    처음에는 단순하게 명세대로 구현.
    하지만 시간초과 발생 -> (사실 당연한 문제..)

    1. 마지막에만 추가할 수 있도록 하는 방법
    2. 중간 삽입에도 시간이 오래걸리지 않는 방법

    을 고민해야하는 문제

    stack 두개를 이용하여 문제 풀이
'''

import sys
from collections import deque

lstack = list(input())
rstack = deque()
N = int(input())

for _ in range(N):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == 'L' and len(lstack) > 0:
        rstack.appendleft(lstack.pop())
    
    elif cmd[0] == 'D' and len(rstack) > 0:
        lstack.append(rstack.popleft())
    
    elif cmd[0] == 'B' and len(lstack) > 0:
        lstack.pop()
    
    elif cmd[0] == 'P':
        lstack.extend(list(cmd[1]))

    # print(lstack)
    # print(rstack)

lstack.extend(rstack)
print("".join(lstack)) 



# import sys

# arr = list(input())
# cur = len(arr)
# # print(cur)
# # print(arr)
# M = int(sys.stdin.readline())

# for _ in range(M):
#     cmd = sys.stdin.readline().split()
#     # print(cmd, cur)

#     if cmd[0] == 'L':
#         if cur > 0:
#             cur -= 1 
#             arr.rotate(1)
#     if cmd[0] == 'D':
#         if cur < len(arr):
#             cur += 1
#             arr.rotate(-1)
#     if cmd[0] == 'P':
#         arr.extend(cmd[1])
#         cur += len(cmd[1])
#     if cmd[0] == 'B':
#         if cur > 0:
#             arr.pop()
#             cur -= 1

#     print(cur)
#     print(arr)

# print("".join(arr))
