'''
    0은 빈칸
    1은 벽
    2는 바이러스가 있는 곳

    새로 세울 수 있는 벽이 3개이고, 반드시 3개를 세워야한다.

    BFS로 바이러스가 퍼질 수 있는 곳을 구함
    이후 BFS 함수를 빈칸의 조건을 바꿔가면서 구함
'''

import sys

def BFS(i, j):
    return

def solution(arr):
    global visit

    for i in range(len(arr)):
        for j in range(len(arr)):
            if visit[i][j] == 1:
                BFS(i,j)
    

if __name__ == "__main__":
    N, M = map(int, input().split())
    
    arr = [] 
    for _ in range(M):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
    visit = [ [0 for _ in range(len(arr))] for _ in range(len(arr)) ]
    solution(arr)