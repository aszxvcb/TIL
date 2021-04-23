'''
    dp : 현재 위치를 오른쪽 끝으로 하는 정사각형의 크기

    010000        010000
    011110        011110
    011110        012220
    011100        012300
    000010        000010

    첫행과 첫열은 matrix를 참고하여 초기화
    다른 좌표는 왼쪽, 왼쪽위, 위를 비교해서
    가능한 정사각형의 크기를 찾는다.

    # 틀린 이유
    정사각형의 넓이를 구해야해서 최종적으로 넓이 계산이 필요
'''

def solution( matrix, n, m ):
    max_val = 0
    dp = [[0]*m for _ in range(n)]
    # print("*" * 10 )
    # for line in dp:
    #     print(line)

    dp[0] = matrix[0]
    if max_val < max(dp[0]):
        max_val = max(dp[0])
    
    for i in range(1, n):
        for j in range(0, m):
            # 첫번째 열은 원본과 같음
            if j==0:
                dp[i][j] = matrix[i][j]
            # 다른 위치들은 해당 위치를 정사각형의 오른쪽 끝인 경우일때 정사각형의 크기 계산
            else:
                if matrix[i][j]==1:
                    # 왼쪽, 왼쪽위, 위의 dp값 확인
                    min_val = min([dp[i][j-1], dp[i-1][j-1], dp[i-1][j]])
                    dp[i][j] = min_val+1
                    
            if max_val < dp[i][j]:
                max_val = dp[i][j]

    # print("*" * 10 )
    # for line in dp:
    #     print(line)

    return max_val

if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append( list(map(int, list(input()))) )
    # for line in matrix:
    #     print(line)

    ret = solution(matrix, n, m)
    print(ret*ret)

