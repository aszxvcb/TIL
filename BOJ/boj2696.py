'''
    boj1655 와 같은 문제 
    중앙값을 구하기위해 힙을 두개 (최대힙, 최소힙)을 사용한다.

    최대힙의 경우 val를 음수로 바꿔줘야함
'''

import sys, heapq

def solution(arr):
    # arr를 순서대로 읽으면서, 홀수번째를 읽을 때마다 중앙값을 출력
    answer = []
    maxHeap = []
    minHeap = []

    for idx, val in enumerate(arr):
        if len(maxHeap) == len(minHeap):
            heapq.heappush(maxHeap, -val)
        elif len(maxHeap)-1 == len(minHeap):
            heapq.heappush(minHeap, val)

        if len(maxHeap) > 0 and len(minHeap) > 0 and \
            minHeap[0] < -maxHeap[0]:
            tempMin = heapq.heappop(minHeap)
            tempMax = -heapq.heappop(maxHeap) 
            heapq.heappush(minHeap, tempMax)
            heapq.heappush(maxHeap, -tempMin)

        if (idx-1)%2 == 1:
            answer.append(-maxHeap[0])

    return answer


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        arr = []
        size = int(sys.stdin.readline())
        while len(arr) != size:
            arr.extend(list(map(int, sys.stdin.readline().split())))
        # print(arr)

        ret = solution(arr)
        print(len(ret))
        for idx, val in enumerate(ret):
            if idx != 0 and idx % 10 == 0:
                print()
            
            print(val, end=' ')
    