# 소가 길을 건너간 이유

'''
    들어온 시간 순으로 정렬
    queue에서 빨리 들어온 순으로 처리

    가능한 케이스
        아직 소가 입장하지 않았다면,
            소가 입장하자마자 검사를 받을 수 있음
                시간 = 소의 입장시간 + 검진에 걸리는 시간
        소가 기다리는 상황이라면 (시간이 입장시간을 넘김 상황)
            시간 = 시간 + 검진에 걸리는 시간
'''

from collections import deque

def solution(arr):
    arr.sort()
    time = arr[0][0]
    queue = deque(arr)

    for cow in queue:
        if time <= cow[0]:
            time = cow[0]+cow[1]
        else:
            time += cow[1]
        # print(time)

    return time

if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append( list(map(int,input().split())) )

    ret = solution(arr)
    print(ret)
