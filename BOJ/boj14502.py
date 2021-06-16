'''
    0은 빈칸
    1은 벽
    2는 바이러스가 있는 곳

    새로 세울 수 있는 벽이 3개이고, 반드시 3개를 세워야한다.
    
    벽은 조합으로 가능한 경우를 찾음
    BFS로 바이러스가 퍼질 수 있는 곳을 구함
    이후 BFS 함수를 빈칸의 조건을 조합의 결과에서 가져와 바꿔가면서 구함

    모든 경우를 탐색하는 브루트포스
    pypy 로 컴파일해서 제출
'''

import sys
from queue import deque
from itertools import combinations
from time import sleep
from copy import deepcopy

def virus(origin_arr, flag):
    global visit

    arr = deepcopy(origin_arr)
    visit = [ [0 for _ in range(len(arr[0]))] for _ in range(len(arr)) ]

    queue = []
    queue = deque(queue)
    
    # 바이러스의 퍼짐을 계산하기위에 큐에 삽입
    for i in range(len(arr)):
            for j in range(len(arr[1])):
                if arr[i][j] == 2:
                    queue.append([i,j])

    while(queue):
        move_x = [-1, 0, 1 ,0]
        move_y = [0, 1, 0, -1]

        cur = queue.popleft()
        # print(cur)
        visit[cur[0]][cur[1]] = 1
        
        for di in range(4):
            dx = cur[0] + move_x[di]
            dy = cur[1] + move_y[di]

            if dx >= 0 and dx < len(arr) and \
                dy >= 0 and dy < len(arr[0]) and \
                    arr[dx][dy] == 0 and visit[dx][dy] == 0:
                    # dx, dy가 범위안에 있고, 바이러스가 퍼질 수 있다면

                    queue.append([dx,dy])
                    arr[dx][dy] = 2

    # if flag == 1:
    #     print("*" * 10)
    #     for line in arr:
    #         print(line)
    #     sleep(4)

    zero_cnt = 0
    for line in arr:
        zero_cnt += line.count(0)

    return zero_cnt

if __name__ == "__main__":
    answer = 0
    N, M = map(int, input().split())
    
    arr = []
    empty_area = []
    for i in range(N):
        data = list(map(int, sys.stdin.readline().rstrip().split()))
        arr.append(data)
        for j in range(M):
            if data[j] == 0:
                empty_area.append([i,j])
    
    ## 가능한 조합 의 경우 계산
    com_arr = combinations(empty_area, 3)
    for com in com_arr:
        # print(list(com))
        flag = 0
        if list(com) == [[5,0],[6,1],[7,2]]:
            # print(list(com))
            flag = 1
            # sleep(4)

        for elem in com:
            arr[elem[0]][elem[1]] = 1
        cnt = virus(arr, flag)
        if answer < cnt:
            answer = cnt
        
        for elem in com:
            arr[elem[0]][elem[1]] = 0

    print(answer)