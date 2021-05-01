'''
    PriorityQueue 또는 heapq를 사용하여 풀이
    heapq가 조금더 빠르다고 함
    입력을 input()으로 받아서 시간초과 났던 문제
    
    값을 push 시 음수로 넣어주면 최대힙처럼 사용할 수 있다.
'''

# from queue import PriorityQueue

# if __name__ == "__main__":
#     N = int(input())
#     PQ = PriorityQueue()
#     for _ in range(N):
#         num = int(input())
        
#         if num == 0:
#             if PQ.empty() == True:
#                 print(0)
#             else:
#                 print(-PQ.get())
#         else:
#             PQ.put(-num)

import heapq
import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    PQ = []
    for _ in range(N):
        num = int(sys.stdin.readline())

        if num == 0:
            if len(PQ) == 0:
                print(0)
            else:
                print(-heapq.heappop(PQ))
        else:
            heapq.heappush(PQ, -num)