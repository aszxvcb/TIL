
'''
    현재 바라보는 방향 기준으로 왼쪽으로 돌아가면서 탐색
    청소가 가능한 곳이면 그 방향으로 전진
    청소가 불가능한 곳이라면 왼쪽으로 회전

    - 구현 문제
    바라보고 있는 방향을 고려해야해서 조건이 까다로운 편
    하지만, 주어진 조건대로 천천히 구현하면 풀 수 있는 난이도

    row, column
    범위 벗어나는 조건문을 헷갈리지 않는 것이 중요
'''

import sys
from time import sleep

def solution():
    global arr, r, c, d
    
    cnt = 0
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    
    if d == 1:
        d = 3
    elif d == 3:
        d = 1

    while(True):
        # print(r, c, d)
        if arr[r][c] == 0:
            cnt += 1
            arr[r][c] = 2

        for idx in range(4):
            nx = r + dx[(d + idx) % 4]
            ny = c + dy[(d + idx) % 4]

            # print(idx, nx, ny)
            if ( 0 <= nx and nx < len(arr)) and ( 0 <= ny and ny < len(arr[0]) ):
                if arr[nx][ny] == 0:
                    r = nx
                    c = ny
                    d = (d + idx) % 4 + 1
                    break

        else:
            # 후진
            # print("후진")
            r = r + dx[ (d-3) % 4 ]
            c = c + dy[ (d-3) % 4 ]
            if (0 <= r and r < len(arr)) and ( 0 <= c and c < len(arr[0])):
                if arr[r][c] == 1:
                    return cnt
            else:
                return cnt


if __name__ == "__main__":
    N, M = map(int, input().split())
    r,c,d = map(int, input().split())

    arr = []
    for _ in range(N):
        arr.append( list(map(int, sys.stdin.readline().rstrip().split())) )
    
    ret = solution()
    print(ret)