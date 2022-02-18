'''
9 3
1 2 3 4 5 6 7 8 9

17

이진탐색/매개변수탐색
디스크의 길이를 절반씩 줄여나가고, 정답을 찾아감

시간초과: reduce 로 매번 배열의 크기를 계산하는 로직을 삭제
틀렸습니다: 시간이 최대값보다 작으면 시간을 늘려줌
'''
from functools import reduce
from copy import deepcopy
from time import sleep

def solution(blueray_num, arr):

    L = 1
    R = reduce(lambda acc, cur: acc + cur, arr, 0)
    max_elem = max(arr)
    mid = 1
    min_mid = R
    while( L < R ):
        if (L+R)//2 != mid:
            mid = (L+R)//2
        else:
            break

        # print(L, R, mid)

        root = []
        child = []
        sum_child = 0
        for elem in reversed(arr):

            if mid < max_elem:  # 가장 큰 값보다 시간이 짧다면, 시간을 늘려준다.
                L = mid
                break
            
            # elem이 추가되었을때, mid보다 크다면 따로 묶어준다.
            if sum_child + elem > mid:
                root.append(deepcopy(child))
                sum_child = elem
                child = [elem]
            else:
                sum_child = sum_child + elem
                child.append(elem)

            
            if len(root) > blueray_num: # 시간을 짧게 잡았다면, mid를 키운다.
                L = mid
                break
        else:
            root.append(deepcopy(child)) # 남은 수를 다 묶어놓음

            if len(root) <= blueray_num:
                R = mid # 시간을 길게 잡았다면, mid를 줄인다.

                if min_mid > mid:
                    min_mid = mid
            else:
                L = mid
            

        # print(root)
        # print()
        # sleep(1)

    print(min_mid)


if __name__ == "__main__":
    blueray_num = list(map(int, input().split()))[1]
    arr = list(map(int, input().split()))

    solution(blueray_num, arr)
