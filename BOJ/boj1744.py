'''
    -1, 0, 1 을 제외한 숫자 두개씩 묶는다
    음수는 음수끼리, 양수는 양수끼리 묶는다
    절댓값이 큰 두 수를 곱해야 크기가 커진다.

    -가 하나 남고 -1 이 있을떄는 곱해서 +를 더해줌
    -가 하나 남고 0 이 있을때는 곱해서 -를 없애줌
    ** 이 조건은 -1,0 도 포함

    ====

    답안을 보고 정리
    양수와 음수, 0을 구분하여 우선순위 큐에 저장
    
    양수
        두개씩 묶으면 더한 것보다 커짐
        1이 포함된 경우는 더하는 것이 큼
    음수
        절대값이 큰 두개를 묶으면 양수가 되어 커짐
        
''' 

import sys, heapq

if __name__ == "__main__":
    N = int(input())
    posHeap = []
    negHeap = []
    tmpHeap = []
    sum_val = 0

    for _ in range(N):
        num = int(sys.stdin.readline().rstrip())
        if num < -1 :
            heapq.heappush(negHeap, num)
        elif num > 1 :
            heapq.heappush(posHeap, -num)
        else:
            heapq.heappush(tmpHeap, num)

    # print(posHeap)
    # print(negHeap)
    # print(tmpHeap)

    while len(posHeap) > 0:
        if len(posHeap) == 1:
            sum_val += -(heapq.heappop(posHeap))
        else:
            sum_val += heapq.heappop(posHeap) * heapq.heappop(posHeap)


    while len(negHeap) > 0:
        # -1은 음수와 곱해 양수로 만들어 더해줌
        if len(negHeap) == 1:
            if len(tmpHeap) > 0 and tmpHeap[0] == -1:
                heapq.heappop(tmpHeap)
                sum_val += -(heapq.heappop(negHeap))
            elif len(tmpHeap) > 0 and tmpHeap[0] == 0:
                heapq.heappop(tmpHeap)
                heapq.heappop(negHeap)
            else:
                sum_val += heapq.heappop(negHeap)
        else:
            sum_val += heapq.heappop(negHeap) * heapq.heappop(negHeap)

    while len(tmpHeap) > 0:
        if tmpHeap.count(-1) >= 2:
            heapq.heappop(tmpHeap)
            heapq.heappop(tmpHeap)
            sum_val += 1
        elif tmpHeap.count(-1) == 1 and tmpHeap.count(0) > 0:
            heapq.heappop(tmpHeap)
            heapq.heappop(tmpHeap)
        else:
            sum_val += heapq.heappop(tmpHeap)
    
    print(sum_val)