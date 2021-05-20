'''
    모든 정점의 연결관계, 거리를 구해야함 -> 플루이드워셜

    각 인간관계를 1이라고 정해놓고, 거쳐갈 수 있는 모든 연결의 최단거리를 구하면 관계 점수가 나옴
    한 사람의 관계점수에서 최대값을 구하면, 그게 그 사람의 최종 점수가 된다
    모든 사람들의 최종점수에서 가장 작은 값을 구하면, 회장후보의 점수가 되고
    이를 바탕으로 정답을 구한다.
'''

import sys

if __name__ == "__main__":
    
    n = int(input())
    adj = [ [float('INF')]*n for _ in range(n) ]
    dist = [ [0]*n for _ in range(n) ]

    # 비방향성 그래프, 가중치는 1, 인접행렬
    while True:
        a, b = map(int, sys.stdin.readline().rstrip().split())

        if a == -1 and b == -1:
            break
        
        adj[a-1][b-1] = 1
        adj[b-1][a-1] = 1

    # for line in adj:
    #     print(line)
    # print()
    
    # dist 배열 초기화
    for i in range(n):
        for j in range(n):
            if i==j:
                dist[i][j] = 0
            elif adj[i][j]:
                dist[i][j] = adj[i][j]
            else:
                dist[i][j] = float('INF')

    # 플루이드-워셜 알고리즘, 거쳐가는 노드를 k로 두고 정점을 거치는 거리를 구함
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min([dist[i][j], dist[i][k] + dist[k][j]])

        # for line in dist:
        #     print(line)
        # print()

    
    score_arr = []
    for line in dist:
        line_score = max(line)
        score_arr.append(line_score)

    min_score = min(score_arr)
    
    print(min_score, score_arr.count(min_score))
    
    result = []
    for idx, score in enumerate(score_arr):
        if score == min_score:
            result.append(str(idx+1))

    print(" ".join(result))


