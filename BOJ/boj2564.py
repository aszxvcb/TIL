'''
    - 구현

    조건을 잘 파악하는 것이 중요
    
'''
import sys
from time import sleep

def solution(arr, start):    
    dist = dict({1:{}, 2:{}, 3:{}, 4:{}})
    for elem in arr:
        if dist.get(elem[0], None) == None:
            dist[elem[0]] = dict()
        dist[elem[0]][elem[1]] = 0

    # print(dist)

    direction = [1,4,2,3]
    ## 시계방향 탐색
    cur = start
    if cur[0] == 1:   # 북쪽
        cur = [cur[0], cur[1]+1]
    elif cur[0] == 2: # 남쪽
        cur = [cur[0], cur[1]-1]
    elif cur[0] == 3: # 서쪽
        cur = [cur[0], cur[1]-1]
    else:             # 동쪽
        cur = [cur[0], cur[1]+1]

    cnt = 0
    while(cur != start):    # 첫 위치로 돌아올 때까지
        cnt += 1
        # 상점에 다다르면 거리를 저장
        if dist[cur[0]].get(cur[1], None) != None:
            dist[cur[0]][cur[1]] = cnt

        # 각 방향 모서리에서의 처리
        if cur in [[1,W], [2,0], [3,0], [4,H]]:
            cur_dir = direction.index(cur[0])
            cur[0] = direction[(cur_dir+1) % 4]
            
            if cur[0] == 1:   # 북쪽
                cur[1] = 0
            elif cur[0] == 2: # 남쪽
                cur[1] = W
            elif cur[0] == 3: # 서쪽
                cur[1] = H
            else:             # 동쪽
                cur[1] = 0

        if cur[0] == 1:   # 북쪽
            cur = [cur[0], cur[1]+1]
        elif cur[0] == 2: # 남쪽
            cur = [cur[0], cur[1]-1]
        elif cur[0] == 3: # 서쪽
            cur = [cur[0], cur[1]-1]
        else:             # 동쪽
            cur = [cur[0], cur[1]+1]

    ## 반시계방향 탐색
    direction.reverse()
    ## 반시계방향 탐색
    if cur[0] == 1:   # 북쪽
        cur = [cur[0], cur[1]-1]
    elif cur[0] == 2: # 남쪽
        cur = [cur[0], cur[1]+1]
    elif cur[0] == 3: # 서쪽
        cur = [cur[0], cur[1]+1]
    else:             # 동쪽
        cur = [cur[0], cur[1]-1]
        
    cnt = 0
    while(cur != start):    # 첫 위치로 돌아올 때까지
        cnt += 1
        # 상점에 다다르면 거리를 저장
        if dist[cur[0]].get(cur[1], None) != None:
            if dist[cur[0]][cur[1]] > cnt:
                dist[cur[0]][cur[1]] = cnt

        # 각 방향 모서리에서의 처리
        if cur in [[1,0], [2,W], [3,H], [4,0]]:
            cur_dir = direction.index(cur[0])
            cur[0] = direction[(cur_dir+1) % 4]
            
            if cur[0] == 1:   # 북쪽
                cur[1] = W
            elif cur[0] == 2: # 남쪽
                cur[1] = 0
            elif cur[0] == 3: # 서쪽
                cur[1] = 0
            else:             # 동쪽
                cur[1] = H

        if cur[0] == 1:   # 북쪽
            cur = [cur[0], cur[1]-1]
        elif cur[0] == 2: # 남쪽
            cur = [cur[0], cur[1]+1]
        elif cur[0] == 3: # 서쪽
            cur = [cur[0], cur[1]+1]
        else:             # 동쪽
            cur = [cur[0], cur[1]-1]
    

    ## 저장된 거리 합 계산
    answer = 0
    for direction in [1,2,3,4]:
        for key in dist[direction]:
            answer += dist[direction][key]

    # print(dist)
    print(answer)

if __name__ == "__main__":
    W, H = map(int, input().split())
    N = int(input())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))    
    start = list(map(int, sys.stdin.readline().rstrip().split()))

    solution(arr, start)
