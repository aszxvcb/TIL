'''
    우선순위큐
'''

import heapq
from queue import deque

def solution(arr, n, m):
    answer = 0
    heapq.heapify(arr)

    for _ in range(m):
        one = heapq.heappop(arr)
        two = heapq.heappop(arr)

        heapq.heappush(arr, one+two)
        heapq.heappush(arr, one+two)

    while(arr):
        answer += arr.pop()

    print(answer)

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    solution(arr,n,m)