'''
    플루이드-워셜 알고리즘을 이용하여
    연결 관계를 계산하는 문제
'''

import sys
from copy import deepcopy

def solution(arr):

    size = len(arr)

    visit = deepcopy(arr)

    for k in range(size):
        for i in range(size):
            for j in range(size):
                if visit[i][k] == visit[k][j] == 1:
                    visit[i][j] = 1
            
    for line in visit:
        for elem in line:
            print(str(elem) + " ", end="")
        else:
            print()

if __name__ == "__main__":
    N = int(input())
    
    arr = []
    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
    solution(arr)