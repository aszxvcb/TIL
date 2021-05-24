'''
    자신의 키 순서를 정확하게 알기위해서는
    자신을 제외한 모든 노드와의 연관관계가 있어야함
    
    플로이드워셜 알고리즘 이용해서 모든 연관관계를 확인 후
    조건에 맞는 노드의 수를 세어 줌

    pypy 이용

    tip
    1. 3중 포문에서 조건문에 min()을 이용하는 최소가중치 문제처럼
        사용하게되면 min 연산으로 인해 시간초과가 발생한다.
        연관 관계만 알면 되기에, 이에 맞게 사용한다.
'''

import sys

if __name__ == "__main__":
    answer = 0
    N, M = map(int, input().split())

    adj = [[0]*N for _ in range(N)]
    for i in range(N):
        adj[i][i] = 0
    
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        adj[a-1][b-1] = 1

    # for line in adj:
    #     print(line)
    
    for mid in range(N):
        for i in range(N):
            for j in range(N):
                # adj[i][j] = min([adj[i][j], adj[i][mid]+adj[mid][j]])
                if adj[i][mid] == 1 and adj[mid][j] == 1:
                    adj[i][j] = 1

    # for line in adj:
    #     print(line)

    for i in range(N):
        flag = True
        for j in range(N):
            if i != j and \
                adj[i][j] == 0 and \
                adj[j][i] == 0:
                flag = False
        
        if flag:
            answer += 1

    print(answer)