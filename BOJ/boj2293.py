'''
    처음에는 DFS 백트래킹을 해야하나 생각했음 하지만, 
    dp문제 였고
    점화식 세우기가 어려웠음
    감을 못잡아서 정답코드 보고 이해함

    https://velog.io/@juno7803/BOJ-2293-%EB%8F%99%EC%A0%84-1
'''
import sys

def solution(arr, k):
    
    dp = [ 0 for _ in range(k+1) ]
    
    '''
        dp[idx]는
        arr의 i번째 인덱스까지 루프를 돌았을 때
        idx를 만족하는 조합의 수
    '''

    for i in arr:
        for idx in range(len(dp)):
            if idx - i == 0:
                dp[idx] += 1
            elif idx - i < 0:
                continue
            else:
                dp[idx] = dp[idx]+dp[idx-i]
        # print(dp)

    return dp


if __name__ == "__main__":
    n, k = map(int, input().split())

    arr = []
    for _ in range(n):
        arr.append(int(sys.stdin.readline().rstrip()))

    arr.sort()
    ret = solution(arr, k)

    print(ret[-1])