'''
    - 구현

    인접한 세칸 또는 네칸이 바다(.)이면 잠긴다.
    범위 밖의 공간은 다 바다이다. 
    출력하는 지도의 크기는 모든 섬을 포함하는 가장 작은 직사각형
    다 잠겨도 하나는 출력해야함
'''

import sys
from queue import deque
from copy import deepcopy

def solution(arr):
    result = deepcopy(arr)
    land_cnt = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    ## 'X'의 위치를 찾은 후, 바다와 인접한 면의 수를 구함
    for x, line in enumerate(arr):
        for y, elem in enumerate(line):
            if elem == 'X':
                land_cnt += 1
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or len(arr) <= nx or ny < 0 or len(arr[0]) <= ny: 
                        cnt += 1
                    else:
                        # print(nx, ny)
                        if arr[nx][ny] == '.':
                            cnt += 1
                
                else:
                    if cnt >= 3:
                        result[x][y] = '.'
                        land_cnt -= 1

    ## 남은 영역이 없을 때
    if land_cnt == 0:
        print('X')
    else:
        ## 필요없는 영역 자르기
        result = deque(result)
        while( 'X' not in result[0] ):
            result.popleft()
        while( 'X' not in result[-1]):
            result.pop()

        start = 0
        end = len(arr[0]) - 1

        flag = True
        while(flag):
            for row in range(len(result)):
                if result[row][start] == 'X':
                    flag = False
                    break
            else:
                start += 1
            
        flag = True
        while(flag):
            for row in range(len(result)):
                if result[row][end] == 'X':
                    flag = False
                    break
            else:
                end -= 1
        
        ## 출력
        for line in result:
            print(''.join(line[start:end+1]))

    

if __name__ == "__main__":
    R, C = map(int, input().split())
    
    arr = []
    for _ in range(R):
        arr.append(list(sys.stdin.readline().rstrip()))

    solution(arr)
