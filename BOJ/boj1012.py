'''
    영역을 구하는 문제
    
    DFS로 푼 경우, 백준에서 런타임에러 발생.
    함수호출의 뎁스가 설정값보다 높아지기 때문인듯함.
    sys.setrecursionlimit(10 ** 4)
    를 추가하여 설정을 높여주면 통과

    BFS로 푸는 것이 더 적은 함수 호출 뎁스를 가질 것 같음
'''

import sys
sys.setrecursionlimit(10 ** 4)

def DFS(MAP, i, j):
    global visit
    # 상,하,좌,우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    visit[i][j] = 1

    for x,y in zip(dx,dy):
        nx = i+x
        ny = j+y
        if  nx < len(MAP) and ny < len(MAP[0]) \
            and nx >= 0 and ny >= 0 \
            and visit[nx][ny] == 0 and MAP[nx][ny] == 1:
            DFS(MAP, nx, ny)
    

def solution(MAP):
    global visit
    cnt = 0
    # for line in MAP:
    #     print(line)

    for i in range(len(MAP)):
        for j in range(len(MAP[0])):
            if MAP[i][j] == 1 and visit[i][j] == 0:
                DFS(MAP, i, j)
                cnt += 1

                # print("=======check======")
                # for line in visit:
                #     print(line)
                # print("=======check======")

    print(cnt)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())

        MAP = [[0]*N for _ in range(M)]
        visit = [[0]*N for _ in range(M)]

        for _ in range(K):
            m, n = map(int, sys.stdin.readline().split())
            MAP[m][n] = 1

        solution(MAP)
