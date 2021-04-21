'''
    최장증가수열, DP

    전길줄이 서로 교차하지 않으려면,
    B로 연결되는 전선이 한쪽의 방향성을 가져야한다. (줄어들거나, 늘어나거나)

    A 를 배열의 인덱스로 보고, B를 값이라고 보면
    최장증가수열을 찾을 수 있고, 이것이 곧 교차하지 않는 전선의 가장 큰 수를 의미한다.
    (전체 전깃줄 수) - (LIS) = (교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소갯수)
    를 구할 수 있다.
'''

def solution(line, num):

    # LIS 구하기
    line.sort() # A를 인덱스로 보고 B를 밸류로 보기위해 정렬
    dp = [1]*num
    for i in range(num):
        for j in range(i):
            if line[j][1] < line[i][1] and dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1
    
    return num - max(dp)


if __name__ == "__main__":

    N = int(input())
    line = []
    for _ in range(N):
        line.append(list(map(int, input().split())))
    # line = [[1,8], [3,9], [2,2], [4,1], [6,4], [10,10], [9,7], [7,6]]
    
    ret = solution(line, len(line))
    print(ret)

    