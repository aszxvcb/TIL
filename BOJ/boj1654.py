'''
    이분탐색, left, right 를 옮겨가며, 중앙값을 계산

    zeroDivisionError 가 발생해서 mid 값이 0이 되는 경우를 확인할 수 있었고 수정함
    cnt가 N보다 커질 수 있음. 같지만은 않음

    2 7 (1~ 잘못된 값 나올때까지 해봄)
    10
    0
    값 : 1

    2 2
    2
    0
    값 : 1
'''

import sys

def solution(arr, max_val):
    global N
    answer = 0
    left = 0
    right = max_val
    if right == 0:
        print(0)
        exit()

    mid = (left + right)//2 if (left + right)//2 != 0 else 1
    while(left <= right):
        cnt = 0
        
        for elem in arr:
            cnt += elem // mid
        
        ## 나누어진 숫자가 부족하다면, 더 작은 단위로 쪼개야 함
        if cnt < N:
            right = mid-1
        else:
            left = mid+1

        ## 조건을 만족하는 길이 중 최대 길이
        if cnt >= N and answer < mid:
            answer = mid


        # print(left, right, mid)
        if mid == 1:
            break
        mid = (left + right) // 2 if (left+right)//2 else 1

    print(answer)


if __name__ == "__main__":
    K, N = map(int, input().split())
    arr = []
    max_val = 0
    for _ in range(K):
        val = int(sys.stdin.readline().rstrip())
        arr.append(val)
        if val > max_val:
            max_val = val
    
    solution(arr, max_val)

