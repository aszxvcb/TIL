# 꼬인 전깃줄
'''
    전깃줄 문제에서 풀이했던 LIS는 DP 방식으로 구함으로써 
    O(n^2)의 시간복잡도를 가짐

    이 문제의 경우 입력값이 크므로
    이분탐색 방식으로 구해서 O(logn)으로 LIS 를 구해야 함
    LIS는 정렬되어 있기 때문에 이분탐색이 가능함
    하지만 이분탐색 방식은 LIS의 요소를 구할 수는 없음
    LIS의 길이를 구하는데에 최적화 되어있음.
'''
def lowerBound(LIS, num):
    left = 0
    # 이분탐색의 경우 len(LIS)-1 을 하지만, bound를 찾기위해서는 값이 없을때를 대비해서 len() 그대로 사용
    right = len(LIS)
    mid = 0
    while left < right:
        mid = (left+right)//2
        if LIS[mid] < num:
            left = mid+1
        else:
            right = mid
    
    return right


def solution(arr):
    LIS = []
    LIS.append(arr[0])
    for i in range(1,len(arr)):
        idx = lowerBound(LIS, arr[i])
        # print(idx)
        if idx >= len(LIS):
            LIS.append(arr[i])
        else:
            LIS[idx] = arr[i]
        # print(LIS)
    # print(LIS)
    return len(LIS)

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    ret = solution(arr)
    print(len(arr) - ret)