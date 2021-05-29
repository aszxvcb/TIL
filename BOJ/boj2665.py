'''
    BFS를 이용하여 탐색
    (0,0) 부터 (N,N) 까지 탐색하며, 검은 블럭을 만날때마다 카운트하여 기록
    pq를 이용하여 검은블럭을 가장 적게 만나는 순서로 탐색을 진행
    (N,N)에 도착하였을 때, 지나온 검은 블록의 수를 결과로 리턴

    다익스트라 풀이도 가능함
    흰색 블럭을 가중치 0, 검은색 블럭을 가중치 1로 두고
    (N,N)으로 갈 수 있는 가장 짧은 가중치를 리턴
    (근데 가중치 그래프를 어떻게 표현하지?? 아직은 BFS가 더 풀이가 쉬울 것 같음..)
'''

import sys, heapq
import time

def BFS(x,y,visit_black):
    global arr
    pq = []
    visited = [ [ float('INF') for _ in range(len(arr[0])) ] for _ in range(len(arr)) ]

    heapq.heappush(pq, [visit_black,x,y])

    while(pq):
        cur = heapq.heappop(pq)
        x = cur[1]
        y = cur[2]
        visit_black = cur[0]

        # 이미 방문했더라도, 적은 검은블록의 수로 방문할 수 있다면 재방문 가능
        if visited[x][y] <= visit_black:
            continue
        else:
            visited[x][y] = visit_black

        # 목적지에 도착하며 종료
        if x == len(arr)-1 and y == len(arr[0])-1:
            return visit_black
    
        # 왼,위,오,아래
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]

        for di in range(4):
            nx = x + dx[di]
            ny = y + dy[di]
            
            if nx < len(arr) and ny < len(arr[0]) and nx >= 0 and ny >= 0:
                if arr[nx][ny] == '1':
                    heapq.heappush(pq, [visit_black, nx, ny])
                # 다음 블록이 검은 블록이라면, 카운트하여 우선순위큐에 삽입
                else:
                    heapq.heappush(pq, [visit_black+1, nx, ny])


if __name__ == "__main__":

    N = int(input())
    arr = []

    for _ in range(N):
        arr.append(list(sys.stdin.readline().rstrip()))
    
    ret = BFS(0, 0, 0)
    print(ret)