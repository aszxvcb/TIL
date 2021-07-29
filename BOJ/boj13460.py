'''
    출발지 기준으로 움직일 수 있는 방향을 체크하여
    BFS로 탐색

    blue를 움직이기 위해 red의 막힌 방향으로 이동하는 경우도 있음
'''
import sys
from queue import deque
from time import sleep

def checkValidArea(pos, arr):
    if pos[0] > 0 and pos[1] > 0 and pos[0] < len(arr) and pos[1] < len(arr[0]):
        return True
    return False

def BFS(queue):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while(queue):
        elem = queue.popleft()
        red, blue, direction, cnt = elem

        ## 갈 수 있는 방향을 체크하여 큐에 추가
        for i in range(4):
            ## 직전 왔던 방향은 탐색하지 않음
            if (direction in [0,2]) and (i in [0,2]):
                continue
            elif (direction in [1,3]) and (i in [1,3]):
                continue
        
            ## 갈 수 있는 방향 체크
            new_red = [red[0]+dx[i], red[1]+dy[i]]
            new_blue = [blue[0]+dx[i], blue[1]+dy[i]]
            if (checkValidArea(new_red, arr) and checkValidArea(new_blue, arr)):
                if (arr[new_red[0]][new_red[1]] in ['.','O']) or (arr[new_blue[0]][new_blue[1]] in ['.']):
                    ## 선택된 방향의 끝으로 이동
                    update_red = new_red
                    update_blue = new_blue
                    print(new_red, new_blue)
                    
                    # Todo. update_red, blue
                    if u

                    queue.append([update_red, update_blue, i, cnt+1])

        print(queue)
        sleep(0.5)

def solution(arr):
    global N, M, end

    ## Find start position
    red = [-1,-1]
    blue = [-1,-1]
    end = [-1,-1]
    for x in range(N):
        for y in range(M):
            if arr[x][y] == 'O':
                end = [x,y]
            elif arr[x][y] == 'R':
                red = [x,y]
            elif arr[x][y] == 'B':
                blue = [x,y]
    
    print(red,blue,end)

    ## BFS
    # [[red_x,red_y], [blue_x, blue_y], direction, move_cnt]
    queue = deque()
    queue.append([red, blue, -1, 0])

    BFS(queue)


if __name__ == "__main__":
    N, M = map(int, input().split())
    
    arr = []
    for _ in range(N):
        line = (list(sys.stdin.readline().rstrip()))
        arr.append(line)

    solution(arr)