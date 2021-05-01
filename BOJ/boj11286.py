# 절댓값 힙
'''
    heap 푸쉬시 item 매개변수에 (우선순위, 값) 형태로 넣어줄 수 있음
    우선순위를 기준으로 힙정렬을 실시
'''

import sys, heapq

PQ = []
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        if len(PQ) == 0:
            print(0)
        else:
            print(heapq.heappop(PQ)[1])

    else :
        heapq.heappush(PQ, [abs(num),num])
        
    # print(PQ)

    