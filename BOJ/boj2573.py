'''
    각 셀의 상하좌우 체크하여 녹은 빙하 체크
    BFS로 영역 체크

    pypy로 제출
'''

import sys
from copy import deepcopy
from queue import deque

def BFS(queue, arr):
    global visit

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    while(queue):
        target = queue.popleft()
        x = target[0]
        y = target[1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx >= 0 and nx < N and ny >= 0 and ny < M) and arr[nx][ny] != 0 and visit[nx][ny] == 0:
                queue.append([nx, ny])
                visit[nx][ny] = 1

def solution(arr):
    global visit
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    next_arr = deepcopy(arr)
    global visit
    loop_cnt = 0
    while(True):
        visit = [ [ 0 for _ in range(M)] for _ in range(N) ]
        loop_cnt += 1
        ## 1년 후 빙하의 상태
        for x in range(N): 
            for y in range(M):
                if arr[x][y] != 0:
                    cnt = 0
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if (nx >= 0 and nx < N and ny >= 0 and ny < M) and arr[nx][ny] == 0:
                            cnt += 1
                        
                    next_arr[x][y] -= cnt
                    if next_arr[x][y] < 0:
                        next_arr[x][y] = 0

        arr = deepcopy(next_arr)

        ## 빙하의 덩어리 계산
        queue = deque()
        area_cnt = 0
        for x in range(N):
            for y in range(M):
                if visit[x][y] == 0 and arr[x][y] != 0:
                    queue.append([x,y])
                    BFS(queue, arr)
                    area_cnt += 1

        # for line in arr:
        #     print(line)

        # print(area_cnt)

        # for line in visit:
        #     print(line)

        ## 덩어리 수에 따라 다음 행동 판단
        if area_cnt == 0:
            print(0)
            break
        elif area_cnt >= 2:
            print(loop_cnt)
            break


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
    solution(arr)