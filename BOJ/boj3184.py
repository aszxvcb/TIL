# 50분 걸림...
# 영역 찾기 # BFS?
        # 울타리는 -1
        # 방문한 위치는 1, 미방문은 0

# 양, 늑대 수 구하기
from collections import deque

def printMap(MAP):
    for line in MAP:
        print(line)

def BFS(i,j):
    global MAP, MAP2
    queue = deque()
    queue.append([i,j])
    
    # BFS 영역 탐색
    # 중앙,상,하,좌,우
    dx = [0,0,0,-1,1]
    dy = [0,1,-1,0,0]
    sheep = 0
    wolf = 0

    while( len(queue) != 0 ):
        x,y = map(int, queue.popleft())
        for di in range(5):
            nx = x+dx[di]; ny = y+dy[di]
            # print("check ", nx, ny)
            if nx >= 0 and nx < H \
                and ny >= 0 and ny < V \
                and MAP2[nx][ny] == 0:
                
                MAP2[nx][ny] = 1
                queue.append([nx, ny])

                # 양과 늑대 수 카운트
                if MAP[nx][ny] == 'o':
                    sheep += 1
                elif MAP[nx][ny] == 'v':
                    wolf += 1
    
    if sheep > wolf:
        wolf = 0
    else :
        sheep = 0

    return [sheep, wolf]
                    

def solution(H, V, MAP):
    global MAP2
    MAP2 = [[0]*V for _ in range(H)]
    # 울타리 영역 표시
    for i in range(H):
        for j in range(V):
            if MAP[i][j] == '#':
                MAP2[i][j] = -1
    # printMap(MAP2)
    
    # 각 영역을 탐색하면서 늑대, 양의 수를 계산
    answer = [0,0]
    for i in range(H):
        for j in range(V):
            # print("check ", i, j)
            if MAP2[i][j] == 0:
                ret = BFS(i,j)
                answer[0] += ret[0]
                answer[1] += ret[1]

    return answer

if __name__ == "__main__":
    H, V = map(int, input().split())
    MAP = []
    for _ in range(H):
        MAP.append(list(input()))

    ret = solution(H,V,MAP)
    print(ret[0], ret[1])
