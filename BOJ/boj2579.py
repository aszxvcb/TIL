# 계단오르기
'''
    dp[0] : 최적
    dp[1] : 현재 계단이 첫번째 계단일 때 최대값
    dp[2] : 현재 계단이 두번째 계단일 때 최대값
'''

def solution(arr, N):
    dp = [[0]*N for _ in range(3)]
    
    if len(arr) >= 3:
        dp[1][0] = arr[0]
        dp[2][0] = arr[0]
        dp[0][0] = max([dp[1][0], dp[2][0]])
        dp[1][1] = arr[1]
        dp[2][1] = arr[0]+arr[1]
        dp[0][1] = max([dp[1][1], dp[2][1]])

        for i in range(2,N):
            dp[1][i] = arr[i]+dp[0][i-2]
            dp[2][i] = arr[i]+dp[1][i-1]
            dp[0][i] = max([dp[1][i], dp[2][i]])
        # print(dp)
        return dp[0][-1]

    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0]+arr[1]
    elif len(arr) == 0 :
        return 0

if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    
    ret = solution(arr, N)
    print(ret)