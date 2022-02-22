#boj10816
'''
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

3 0 0 1 2 0 0 2
'''
import bisect

def solution(arr, target):
    result = []
    arr.sort()
    for elem in target:
        left = bisect.bisect_left(arr, elem)
        right = bisect.bisect_right(arr, elem)
        result.append(right - left)
    
    print(" ".join(map(str,result)))

if __name__ == "__main__":
    input()
    arr = list(map(int, input().split()))
    input()
    target = list(map(int, input().split()))

    solution(arr, target)