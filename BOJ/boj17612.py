'''
    걸린시간 : 1시간 이상
    
    k의 크기 떄문에 시간초과 발생
    이후 우선순위 큐를 사용해야하는 것 인지
    조건을 만족하게 하는 것이 꽤나 까다로웠던 문제

    최대힙, 최소힙 두개를 사용
'''

import sys, heapq
from collections import deque

def solution(K, queue):
    answer = 0
    cnt = 1
    check = []
    outHeap = []

    # counter 초기화 [짐, 카운터번호, ID]
    counters = [(0,i+1,0) for i in range(K)]
    # print(counters)

    while(counters):
        # 계산이 가장 빨리 끝나는 손님 퇴장
        out = heapq.heappop(counters)
        
        # 빈 계산대가 아니라면
        if out[2] != 0:
            # 멀리 있는 계산대 순서대로 정렬하기 위해서 -out[1] => maxHeap
            heapq.heappush(outHeap, (out[0], -out[1], out[2]))
        
        # 들어올 손님이 있다면, 계산대로 이동
        if len(queue) > 0:
            ID, w = queue.popleft()
            heapq.heappush(counters, (out[0]+w, out[1], ID))
    # print(counters)
    # print(outHeap)

    # 나간 손님 중, 계산이 빨리 끝나고 출구쪽 계산대 손님부터 계산
    for i in range(len(outHeap)):
        answer += (i+1) * heapq.heappop(outHeap)[2]

    # print(answer)
    return answer     

if __name__ == "__main__":
    N, K = map(int, input().split())
    queue = deque([])

    for _ in range(N):
        ID, w = map(int, sys.stdin.readline().split())
        queue.append((ID, w))

    ret = solution(K, queue)
    print(ret)

