'''
    - 그리디
    수업은 시작 순서대로 정렬
    강의실은 우선순위큐를 이용하여 빨리 끝나는 순서대로 정렬
    만약 수업시작 시간이 현재 강의실 중 가장 먼저 끝나는 강의보다 빨리 시작한다면,
    새로운 강의실을 구해야함

    반례 참고 : https://www.google.com/search?q=boj11000&oq=boj11000&aqs=chrome..69i57j0i13.2392j0j7&sourceid=chrome&ie=UTF-8
    수업을 끝나는 시간 기준으로 정렬하게 되면 답이 나오지 않는 경우가 발생

    시간초과 발생
    모든 강의를 확인하는 경우는 시간이 오래 걸림
    heapify 연산은 오래 걸림    

'''

import sys, heapq
from queue import deque

def solution(lectures):
    room = []
    cnt = 0
    while(lectures):
        # lect = heapq.heappop(lectures)
        lect = lectures.popleft()
        # print(lect)

        if len(room) == 0:
            room.append(lect[1])
            cnt += 1
            continue

        '''
        # 모든 강의실을 탐색하면 시간초과 발생
        for idx in range(len(room)):
            if room[idx] <= lect[1]:
                room[idx] = lect[0]
                break
        else:
            room.append(lect[0])
        '''

        # 가장 빨리 끝나는 수업이 새로운 수업보다 늦게 끝난다면, 강의실을 대여
        if room[0] > lect[0]:
            heapq.heappush(room, lect[1])
            cnt += 1
        else:
            '''
            # heapify 하는 과정에서 시간 초과 발생
            room[0] = lect[1]
            heapq.heapify(room)
            '''
            heapq.heappop(room)
            heapq.heappush(room, lect[1])

    # print(room)
    # print(len(room))
    print(cnt)            

if __name__ == "__main__":
    N = int(input())
    
    lectures = []
    for _ in range(N):
        l = list(map(int, sys.stdin.readline().rstrip().split()))
        # 빨리 시작하는 순으로 정렬
        lectures.append(l)

    lectures.sort()
    solution(deque(lectures))
