# boj7795
'''
    A,B를 정렬한 후, B에서 A값들을 키값으로하여 이분탐색.
    bisect.bisect_left, bisect_right 를 이용

2
5 3
8 1 7 3 1
3 6 1
3 4
2 13 7
103 11 290 215

7
1
'''

import bisect

def solution(A, B):
    A.sort()
    B.sort()
    # print(A)
    # print(B)

    sum_cnt = 0 
    for elem_A in A:
        idx = bisect.bisect_left(B, elem_A) - 1
        if B[idx] < elem_A:       # A의 값이 B의 값보다 크다면, 인덱스만큼 더함
            sum_cnt = sum_cnt + (idx+1)
            # print("check1 ", str(idx+1))
        elif B[idx] == elem_A:    # A의 값이 B의 값과 같다면, 인덱스 바로 전까지의 합을 더함
            ## 같은 값이 여러개 있을 수 있으므로, 제외해줌
            if idx > 0:
                sum_cnt = sum_cnt + idx
            # print("check2 ", str(idx))
        else:
            # print("check3 ", str(idx))
            pass

    print(sum_cnt)

if __name__ == "__main__":
    TC = int(input())
    for _ in range(TC):
        num_A, num_B = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        solution(A, B)