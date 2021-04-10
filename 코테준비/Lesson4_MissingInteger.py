def solution(A):
    answer = 0

    A.sort()
    prev_num = 0
    # print(A)
    for i in A:
        if i > 0:
            if i == prev_num:
                continue
            if i == prev_num+1:
                prev_num = i
            else :
                break
    else:
        return prev_num+1