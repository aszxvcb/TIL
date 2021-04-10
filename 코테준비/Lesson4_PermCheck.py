def solution(A):
    A.sort()
    for i in range(1, len(A)+1):
        if not A[i-1] == i:
            return 0
    else:
        return 1