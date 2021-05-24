'''
    1. N개의 배열을 만들어 K, L에 해당하는 인덱스에 0, 나머지에 1을 넣음
    2. 배열에서 두개씩 뽑아 비교
        2-1. 타겟인 L,K 는 자연스럽게 살아남음
        2-2. 홀수개의 경우 부전승
    3. K, L 이 만날때 까지의 갯수를 카운트함
'''
import sys
from collections import deque

def solution(arr, cnt):
    new_arr = deque()

    for _ in range(len(arr)//2):
        left = arr.popleft()
        right = arr.popleft()

        if left == 0 and right == 0:
            print(cnt)
            exit()

        new_arr.append(min([left, right]))
    else:
        if arr:
            new_arr.append(arr.popleft())

    if len(new_arr) != 1:
        solution(new_arr, cnt+1)
    else:
        print(cnt)


if __name__ == "__main__":
    
    N, K, L = map(int, input().split())

    arr = [1] * N
    arr[K-1] = 0
    arr[L-1] = 0

    arr = deque(arr)

    solution(arr, 1)

    

        
