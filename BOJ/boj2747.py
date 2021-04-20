# 피보나치 f(n)을 구하는 문제

def solution(n):
    dp = [0] * 46
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-1]

    # print(dp)

    return dp[n]

if __name__ == "__main__":
    n = int(input())
    ret = solution(n)
    print(ret)