'''
    - deque 을 이용

    양쪽 끝에서 max_value로 탐색을 하며
    점점 큰 value를 가지도록 천장을 구성
'''

import sys, heapq
from queue import deque

def solution(arr, max_key, max_value):
    arr = deque(arr)

    check = [0] * 10001
    min_idx = arr[0][0]
    max_idx = arr[-1][0]
    
    prev_key, prev_value = 0, 0
    ## max_key를 중심으로 점점 커지는 value를 탐색
    while(arr):
        key = arr[0][0]
        # 왼쪽 -> 오른쪽 탐색
        if key < max_key:
            elem = arr.popleft()
        
        # max_key 기준
        elif key == max_key:
            elem = arr.popleft()
            key, value = elem[0], elem[1]

            check[key] = value
            prev_key = 0
            prev_value = 0
            
            continue
        # 오른쪽 -> 왼쪽 탐색
        else:
            elem = arr.pop()

        key, value = elem[0], elem[1]

        if prev_value < value:
            check[key] = value
            prev_key = key
            prev_value = value

    check = check[min_idx : max_idx+1]

    ## 넓이 계산
    for i in range(len(check)):
        if check[i] == 0:
            check[i] = check[i-1]
        elif check[i] == max_value:
            break

    for i in reversed(range(len(check))):
        if check[i] == 0:
            check[i] = check[i+1]
        elif check[i] == max_value:
            break

    # max_value가 중복일 때
    for i in range(len(check)):
        if check[i] == 0:
            check[i] = max_value

    ## answer
    # print(check)
    print(sum(check))

if __name__ == "__main__":
    N = int(input())

    arr = []
    max_key, max_value = 0, 0
    for _ in range(N):
        key, value = map(int,sys.stdin.readline().rstrip().split())
        arr.append([key, value])

        if max_value < value:
            max_value = value
            max_key = key
    arr.sort()

    solution(arr, max_key, max_value)


