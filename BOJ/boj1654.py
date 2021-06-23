import sys

def solution(arr, end):
    global N

    start = 1
    mid = (start + end) // 2
    
    max_val = 0
    while(mid != start and mid != end):
        # print(mid)
        cnt = 0
        max_cnt = 0

        for elem in arr:
            cnt += elem // mid

        # 조건을 만족하는 최대값 저장
        if cnt >= N:
            if mid > max_val:
                max_val = mid
                break
        
        if cnt > N:
            mid = mid + (mid // 2)
            # cnt가 작게 나온다면, mid를 줄여야 함
        else:
            mid //= 2

        if mid == 1:
            break

    print(max_val)

if __name__ == "__main__":
    K, N = map(int, input().split())
    arr = []
    max_val = 1
    for _ in range(K):
        val = int(sys.stdin.readline().rstrip())
        arr.append(val)
        if val > max_val:
            max_val = val
    
    solution(arr, max_val)

