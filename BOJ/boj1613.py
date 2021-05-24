'''

    BFS로 하면 시간초과
    -> 플로이드 워셜로 풀이

    python3 컴파일러로는 시간초과 발생, pypy로 컴파일해서 풀이

'''
import sys

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().rstrip().split())

    # Make visit adj set
    adj = [[float('INF')]*n for _ in range(n)]
    for i in range(n):
        adj[i][i] = 0

    for _ in range(k):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        adj[a-1][b-1] = 1

    # 플로이드-와샬
    for k in range(n):
        for i in range(n):
            for j in range(n):
                adj[i][j] = min([adj[i][j], adj[i][k] + adj[k][j]])

    # for line in adj:
    #     print(line)

    # solution
    s = int(sys.stdin.readline().rstrip())
    for _ in range(s):
        a, b = map(int, sys.stdin.readline().rstrip().split())

        if adj[a-1][b-1] != float('INF'):
            sys.stdout.write(str("-1\n"))
        elif adj[b-1][a-1] != float('INF'):
            sys.stdout.write(str("1\n"))
        else:
            sys.stdout.write(str("0\n"))

'''
# adj, adj_reverse 두개를 두고 푼 풀이
# 시간초과 발생

# adj 하나로 해결할 수 있나?

if __name__ == "__main__":
    n, k = map(int, input().split())

    connect = [ [] for _ in range(n) ]

    # Make visit adj set
    adj = [[float('INF')]*n for _ in range(n)]
    adj_reverse = [[float('INF')]*n for _ in range(n)]
    for i in range(n):
        adj[i][i] = 0
        adj_reverse[i][i] = 0

    for _ in range(k):
        a, b = map(int, input().split())
        adj[a-1][b-1] = 1
        adj_reverse[b-1][a-1] = 1

    # 플로이드-와샬
    for k in range(n):
        for i in range(n):
            for j in range(n):
                adj[i][j] = min([adj[i][j], adj[i][k] + adj[k][j]])
                adj_reverse[i][j] = min([adj_reverse[i][j], adj_reverse[i][k] + adj_reverse[k][j]])

    # for line in adj:
    #     print(line)
    # print("*" * 10)
    # for line in adj_reverse:
    #     print(line)

    # solution
    s = int(input())
    for _ in range(s):
        a, b = map(int, input().split())

        if adj[a-1][b-1] != float('INF'):
            print(-1)
        elif adj_reverse[a-1][b-1] != float('INF'):
            print(1)
        else:
            print(0)
'''

    

'''
    연결 여부만 구하면 됨
    방향성 그래프 저장
    앞뒤 바꿔가며 탐색하면
    연결 여부를 구할 수 있음

    라고 생각하고 BFS로 풀이하였지만, 시간초과 발생

# BFS 시간초과
def bfs(connect, a, b):
    global n
    visit = [False] * n

    queue = deque([a])
    while queue :
        cur = queue.popleft()
        visit[cur-1] = True

        if cur == b:
            return True

        for node in connect[cur-1]:
            if visit[node-1] != True:
                queue.append(node)

    return False

if __name__ == "__main__":
    n, k = map(int, input().split())

    connect = [ [] for _ in range(n) ]

    for _ in range(k):
        a, b = map(int, input().split())
        connect[a-1].append(b)

    print(connect)

    s = int(input())
    for _ in range(s):
        a, b = map(int, input().split())

        if bfs(connect, a, b) :
            print(-1)
        elif bfs(connect, b, a) :
            print(1)
        else:
            print(0)
'''