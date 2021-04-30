'''
    못푼 문제 : 정담 코드 참고

    처음 접근은 DFS로 모든 계산 결과를 탐색하여 최종적으로 원하는 값이 나오는 경우를 세어주는 방식으로 접근
    하지만 시간초과 발생 -> O(2^N) 의 연산이 필요

    문제유형이 DP 임을 확인하고도 풀이방법이 떠오르지 않아 해설을 참고
    dp[i][j]=k 는 i 인덱스의 계산결과 j가 나오는 갯수 k 라고 정의하면
    dp[i][j] = dp[i-1][j-arr[i]] + dp[i-1][j+arr[i]] 가 된다.
    (이때 j-arr[i]가 0보다 크고 20보다 작은 조건을 만족해야 함)
    
    계산결과가 0~20 사이에서 나오므로 중복된 결과가 나올 수 있음.
    이를 메모이제이션 기법을 사용하면 중복계산을 줄일 수 있음
'''

result = 0
cnt = 0

def DFS(curNum, idx):
    global result, cnt
    # print(curNum, arr, idx)
    if idx < len(arr):    
        if curNum + arr[idx] <= 20:
            DFS(curNum+arr[idx], idx+1)

        if curNum - arr[idx] >= 0:
            DFS(curNum-arr[idx], idx+1)

    if idx == len(arr) and curNum == result:
        cnt += 1


def solution(): # 시간초과
    global result, arr
    result = arr[-1]
    arr = arr[:-1]
    print(arr)
    DFS(0, 0)
    
def solution2(arr):
    result = arr[-1]
    numbers = arr[:-1]

    dp = [[0]*21 for _ in range(len(numbers))]

    dp[0][arr[0]] = 1
    for i in range(1,len(numbers)):
        for j in range(21):
            if j-numbers[i] >= 0:
                dp[i][j] += dp[i-1][j-numbers[i]]
            if j+numbers[i] <= 20:
                dp[i][j] += dp[i-1][j+numbers[i]]

    # for line in dp:
    #     print(line)

    return dp[len(numbers)-1][result]
    

if __name__ == "__main__":
    N = input()
    arr = list(map(int, input().split()))

    ''' DFS 풀이 -> 시간초과 '''
    # solution()
    # print(cnt)

    ret = solution2(arr)
    print(ret)
    
