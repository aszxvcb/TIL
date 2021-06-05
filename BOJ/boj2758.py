'''
    점화식을 어떻게 세워야할지 모르겠다.
    DFS와 백트래킹을 이용해서 정확도는 맞추는 것 같은데
    시간초과 발생.

    답안을 보기위해 정답 코드 복붙

'''

import sys

def dfs(num, i):
    global n, m, cnt, max_val

    # print(num, i)
    if num == n :
        cnt += 1

    elif num < n:
        for j in range(i*2, max_val[num+1]+1):
            dfs(num+1, j)
    
    else:
        return


def solution(n, m):
    global max_val

    for i in range(n,0,-1):
        max_val[i] = m
        m //= 2
    # print(max_val)

    dfs(1, 1)
    

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        cnt = 0
        max_val = {}
        n, m = map(int, sys.stdin.readline().rstrip().split())
        solution(n, m)
        print(cnt)
        