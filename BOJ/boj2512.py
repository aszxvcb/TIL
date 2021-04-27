# 예산
'''
    파라메트릭 서치
'''

def solution(arr, budget):
    start = 0
    end = max(arr)
    max_mid = 0

    while start <= end:
        sum_val = 0
        mid = (start + end) // 2
        
        for elem in arr:
            if elem > mid:
                sum_val += mid
            else:
                sum_val += elem
        # print(sum_val, mid)
        
        if sum_val > budget:
            end = mid - 1
        elif sum_val < budget:
            start = mid + 1
        else :
            max_mid = mid
            break
    
        if sum_val <= budget and max_mid < mid:
            max_mid = mid
  
    return max_mid
        

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    budget = int(input())

    ret = solution(arr, budget)
    print(ret)