'''
    BFS 를 이용한 다소 복잡한 구현 문제

    - 상어의 처음 위치를 탐색
    - BFS를 이용하여 최단거리에 있는 먹을 수 있는 물고기 탐색
    - 물고기들 중 조건에 맞는 물고기 하나 선별
    - 선별한 물고기까지의 거리 덧셈
    - 먹은 물고기 수를 체크하여 상어의 크기 결정
'''

import sys
from queue import deque

# 먹을 수 있는 물고기인지 체크
def size_check(nx, ny, max_size):
    global arr
    return arr[nx][ny] < max_size

# BFS 범위를 벗어나지 않는지 체크
def inner_check(nx, ny):
    global N
    return nx >= 0 and nx < N and ny >= 0 and ny < N

# BFS를 이용한 탐색
def BFS(arr, i, j, max_size):
    global N

    visit = [ [ 0 for _ in range(N)] for _ in range(N) ]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    queue = deque([[i,j,0]])
    
    near = []
    while(queue):
        cur = queue.popleft()
        # print(cur)
        step = cur[2]
        for di in range(4):
            nx = cur[0]+dx[di]
            ny = cur[1]+dy[di]
            if inner_check(nx,ny) and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                # 0 이거나 크기가 같은 경우, step을 증가하고 queue 에 넣어 줌
                if arr[nx][ny] == 0 or arr[nx][ny] == max_size:
                    queue.append([nx, ny, step+1])
                    # print(queue)
                # 물고기인 경우, 크기를 체크하여 보관
                else:
                    if size_check(nx, ny, max_size) and ( len(near) == 0 or near[0][2] >= step+1 ):
                        near.append([nx, ny, step+1])
                            
    return near


# 상어의 초기위치 탐색
def find_shark(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 9:
                return [i,j]


def solution(arr):
    step = 0
    max_size = 2
    num_fish = 0

    # 현재 상어의 위치 탐색
    cur = find_shark(arr)
    arr[cur[0]][cur[1]] = 0
    
    while(True):
        # BFS로 가장 가까운 거리의 먹을 수 있는 물고기 탐색    
        near = BFS(arr, cur[0], cur[1], max_size)
        # print(near)
        if len(near) == 0:
            break
        
        # 조건에 맞는 물고기 선별 및 거리 계산
        near.sort()
        cur[0], cur[1] = near[0][0], near[0][1]
        step += near[0][2]
        arr[cur[0]][cur[1]] = 0
        
        # 먹은 물고기 수를 체크하여 상어의 크기 계산
        num_fish += 1
        if num_fish == max_size:
            max_size += 1
            num_fish = 0
    
    print(step)
    # for line in arr:
    #     print(line)

        

if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # for line in arr:
    #     print(line)

    solution(arr)