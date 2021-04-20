'''
    초기 dp 배열을 만들고
    SK가 1,3,4 중 선택했을 때
    CY 입장에서 지는 경기가 존재한다면,
    SK는 그 인덱스를 선택할 것임.
    게임은 SK가 승리
'''

def solution(N):
    dp = [0,1,0,1,1]

    for i in range(5, N+1):
        if dp[i-1] == 0 or dp[i-3] == 0 or dp[i-4] == 0:
            dp.append(1)
        else:
            dp.append(0)
    
    if dp[N] == 1: print("SK")
    else : print("CY")

if __name__ == "__main__":
    N = int(input())
    solution(N)