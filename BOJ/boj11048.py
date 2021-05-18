'''
    DP로 많이 볼수 있었던 기본 예제
'''

import sys

def solution(arr, N, M):
    # dp[i][j] 는 (i,j)까지 올 수 있는 거리 중 최대값
    dp = [ [0]*M for _ in range(N) ]

    # 이동할 수 있는 경로 설정
    dx = [1,1,0]
    dy = [0,1,1]
    
    for i in range(N):
        for j in range(M):
            # 초기값 설정
            if i==0 and j==0:
                dp[i][j] = arr[0][0]
            
            for k in range(3):
                nx = i+dx[k]
                ny = j+dy[k]

                # 경계값 체크
                if nx >= N or ny >= M:
                    continue
                
                # 대소 비교
                if dp[nx][ny] < dp[i][j]+arr[nx][ny]:
                    dp[nx][ny] = dp[i][j]+arr[nx][ny]

    # for line in dp:
    #     print(line)

    print(dp[N-1][M-1])                

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        line = list(map(int, sys.stdin.readline().rstrip().split()))
        arr.append(line)

    solution(arr, N, M)

