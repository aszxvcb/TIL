'''
    부분합??
    조합??
'''
from itertools import combinations

if __name__ == "__main__":
    N, M = map(int, input().split())
    idx = [ i for i in range(N) ]
    # arr = list(map(int, input().split()))
    # print(arr)

    com_arr = list(combinations(idx, M))
    # print(com_arr)
    print(3)


    