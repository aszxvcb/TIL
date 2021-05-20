'''
    트리 표현을 어떻게 하지? 트리 클래스를 만들어야하나?

    인접행렬로 표현가능
    BFS로 최단거리를 구하면 되는 문제

    형제들과는 2촌
'''

import sys
from collections import deque

def BFS(adj, start, end):
    answer = float('INF')

    # 방문 노드
    global n
    visit = [ False ] * n
    count = 0

    queue = deque()
    queue.append([start, count])
    
    while(queue):
        cur = queue.popleft()
        visit[cur[0]-1] = True
        
        if cur[0] == end and cur[1] < answer:
            answer = cur[1]
        
        for node in adj[cur[0]-1]:
            if visit[node-1] == False:
                queue.append([node, cur[1]+1])

    if answer != float('INF'):
        print(answer)
    else:
        print(-1)

if __name__ == "__main__":
    n = int(input())
    a, b = map(int, input().split())
    m = int(input())

    # 인접행렬
    adj = [ [] for _ in range(n) ]

    for _ in range(m):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        adj[x-1].append(y)
        adj[y-1].append(x)

    BFS(adj, a, b)

        



