'''
    누적합과 lowerBound를 이용한 문제

    https://awesomeroo.tistory.com/30?category=743193
    lowerBound : 키값과 같거나 큰 수가 나오는 위치를(right) 리턴
    upperBound : 키값보다 큰 수가 나오는 위치를 리턴

    다른풀이를 보니, 입력 배열에서 투포인터를 이용하여 푼 풀이도 존재함
'''

# 투포인터
def solution2(S, arr):
    left = 0
    right = 0
    sum_val = arr[0]
    min_interval = float('INF')

    while left <= right and right < len(arr):
        print(left, right, sum_val)
        if sum_val < S:
            right += 1
            if right >= len(arr):
                break
            sum_val += arr[right]
        elif sum_val == S:
            interval = right - left + 1
            min_interval = interval if min_interval > interval else min_interval
            
            right += 1
            if right >= len(arr):
                break
            sum_val += arr[right]
        elif sum_val > S:
            interval = right - left + 1
            min_interval = interval if min_interval > interval else min_interval
            
            sum_val -= arr[left]
            left += 1


    if min_interval == float('INF'):
        return 0
    else:
        return min_interval
            
# 누적합
def solution(S, arr):
    min_val = float('INF')
    sum_arr = [0]
    # 누적합
    for idx in range(len(arr)):
        if len(sum_arr) > 0:
            sum_arr.append(sum_arr[-1]+arr[idx])
        else:
            sum_arr.append(arr[idx])

    # print(sum_arr)

    # lowerBound 인덱스 찾고 기록
    for idx in range(len(sum_arr)):
        target = S + sum_arr[idx]
        
        left = 0
        right = len(sum_arr)
        while(left<right):
            mid = (left + right) // 2
            if sum_arr[mid] == target:
                right = mid
            elif sum_arr[mid] > target:
                right = mid
            else:
                left = mid+1
        
        # print(target, right)

        # lowerBound가 존재한다면
        if right != len(sum_arr):
            if min_val > right - idx:
                # print("check ", right, idx)
                min_val = right - idx
        
    # print(min_val)
    if min_val != float('INF'):
        return min_val
    else:
        return 0
        


if __name__ == "__main__":
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    # ret = solution(S, arr)
    ret = solution2(S, arr)
    print(ret)