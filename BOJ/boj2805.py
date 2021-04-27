# 나무 자르기
'''
    이분탐색(정확하게는 파라메트릭서치)으로 절단기의 위치를 절반씩 조정해나감
'''
global M

def solution(tree):
    global M
    sum_num = 0
    start = 0
    end = max(tree)
    mid = (start + end) // 2
    max_mid = 0

    while start != mid and end != mid:
        sum_num = 0
        # ''' 자른 나무길이의 합 계산 '''
        for t in tree:
            if t > mid:
                sum_num += t - mid
        # print(sum_num, start, end, mid)

        # ''' 자른 나무가 모자르면, 절단기를 왼쪽으로 '''
        if sum_num < M:
            end = mid
        # ''' 자른 나무가 너무 많으면, 절단기를 오른쪽으로 '''
        elif sum_num > M:
            start = mid
        # ''' 일치하면 최적 '''
        else:
            return mid

        # ''' 절단기의 최대위치 갱신 '''
        if sum_num >= M and max_mid < mid:
            max_mid = mid

        mid = (start + end) // 2

    return max_mid

if __name__ == "__main__":
    global M
    N, M = map(int, input().split())
    tree = list(map(int, input().split()))
    
    mid = max(tree)//2
    ret = solution(tree)
    print(ret)