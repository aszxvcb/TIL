# N번째 큰 수를 구하기
# 입력되는 배열의 크기가 N*N 이고 N은 1500 까지 가능함
'''
    메모리 부족으로 다시 풀었던 문제

    최대길이가 N인 최소힙을 만들고
    현재 최소힙의 최솟값보다 큰 값이 들어오면,
    최소값과 현재값을 스왑한다.

    반복문이 돌고나면 최소힙에는 큰수들만 들어오게되고 top에는 N번째로 큰
    (= N개의 큰수들 중 가장 작은) 수가 오게된다.
'''

import sys, heapq

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    minHeap = []
    for _ in range(N):
        line = list(map(int, input().split()))
        for num in line:
            if len(minHeap) < N:
                heapq.heappush(minHeap, num)
            else:
                if num > minHeap[0]:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, num)
    
    print(minHeap[0])



''' 메모리 부족
import sys, heapq

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    maxHeap = []
    arr = []
    row_arr = [col for col in range(N)]
    for idx in range(N):
        line = list(map(int, sys.stdin.readline().split()))
        col_arr = [idx]*N 
        line = list(zip(line, col_arr, row_arr))
        arr.append( line )
    
    # for line in arr:
    #     print(line)

    # 마지막 행을 힙에 넣음
    line = list(map(lambda x: (-x[0], [x[1], x[2]]), arr[N-1]))
    maxHeap.extend(line)
    heapq.heapify(maxHeap)
    for _ in range(N-1):
        maxValue = heapq.heappop(maxHeap)
        # print(maxValue)
        if maxValue[1][0] > 0:
            temp = arr[maxValue[1][0]-1][maxValue[1][1]]
            elem = (-temp[0], [temp[1],temp[2]])
            heapq.heappush(maxHeap, elem)
    # print(maxHeap)

    print(-(heapq.heappop(maxHeap)[0]))

    '''