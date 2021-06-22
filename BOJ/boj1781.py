'''
    데드라인 순으로 정렬하고, 그 중 컵라면의 수가 가장 큰 것 먼저 문제를 해결 (X)
        데드라인    1   2   3   4   4   4
        컵라면수    1   1   1   1   5   5
        예상 값 : 12
        결과 값 : 8

    데드라인 안에서 해결할 수 있는 것들 중 컵라면의 수가 가장 큰 것을 먼저 해결 (X)
        데드라인    1   2   3   4   4   4   
        컵라면수    4   4   4   1   5   5
        예상 값 : 18
        결과 값 : 15

    현재의 보상을 포기하고, 미래의 값을 취할 때, 더 큰 이득을 가지는 경우가 생김
    데드라인이 짧은 순서대로 값을 취하되,
    데드라인이 같은 문제들 중, 보상이 큰 문제가 들어온다면
    이전에 취했던 문제들 중 가장 작은 하나를 빼고, 새로운 문제를 받아들인다.

'''

import sys
from queue import deque
import heapq

def solution(arr):
    pq = []
    answer = 0
    time = 0

    for i in range(len(arr)):
        arr[i][1] *= -1

    arr.sort()

    arr = deque(arr)
    while(arr):
        elem = arr[0]
        deadline = elem[0]
        cup = elem[1]

        # print(elem, time, pq)
        if deadline > time:
            heapq.heappush(pq, -cup)
            time += 1
        elif len(pq) > 0 and pq[0] < -cup:
            heapq.heappop(pq)
            heapq.heappush(pq, -cup)

        arr.popleft()

    for elem in pq:
        answer += elem
    
    return answer

if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
    ret = solution(arr)
    print(ret)