'''
    DP 문제
    각 단계에서 갈 수 있는 곳을 확인하면서 최솟값을 갱신

    arr = [3,5,2,2,1,1,1] 일 때
    dp = [INF,INF,INF,INF,INF,INF,INF] 
    arr의 인덱스를 i라고 할 때,

    i가 0일 때,
    arr[0] = 3 이고
    dp = [0, 1, 1, 1, INF, INF, INF]
    가 된다.

    i가 1일 때,
    arr[1] = 5 이고
    dp = [0, 1, 1, 1, INF, INF, INF] 에서
    dp = [0, 1, min(1,2), min(1,2), 2, 2, 2]
    dp = [0, 1, 1, 1, 2, 2, 2]

    i가 2일 때, 
    arr[2] = 2 이고
    dp = [0, 1, 1, min(1,2), min(1,2), 2, 2]
    dp = [0, 1, 1, 1, 1, 2, 2]

    ... 반복하면 마지막 인덱스가 최적의 횟수가 된다.
'''
def solution(arr, N):
    dp = [float('INF')]*N
    dp[0] = 0
    for i in range(N):
        for j in range(i+1, (i+1)+(arr[i])):
            if j >= N:
                break
            dp[j] = min([dp[j], dp[i]+1])
        # print(dp)
    
    if dp[N-1] == float('INF'):
        return -1
    else:
        return dp[N-1]
            

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    # N = 7
    # arr = [3,5,2,2,1,1,1]
    ret = solution(arr, N)
    print(ret)
    