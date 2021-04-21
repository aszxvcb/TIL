'''
    dp배열의 값을 승리여부로 정의한다면
        dp[0] = 상대방의 승리
        dp[1] = 나의 승리
        dp[2] = 상대방의 승리
        dp[3] = 나의 승리
    로 초기화가 가능하다

    dp[4]의 경우, dp[4-1], dp[4-3]으로 변경할 수 있고,
    이때의 dp값이 결과가 되어준다.
'''

def solution(N):
    if N % 2 == 0:
        print("CY")
    else:
        print("SK")

if __name__ == "__main__":
    N = int(input())
    solution(N)