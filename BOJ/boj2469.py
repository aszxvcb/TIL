'''
    - 구현

    ???을 기준으로
        위에서의 결과를 계산
        아래에서의 결과를 계산

    계산 결과를 바탕으로 ???에 들어올 수 있는 경우를 계산

'''

import sys

def solution():
    global arr, k, n, dest
    answer = []
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    start = alphabet[0:k]
    question_line = 0

    for x in range(n):
        # ? 위에까지만 결과 계산
        if arr[x][0] == '?':
            question_line = x
            break
        else:
            for y in range(k-1):
                if arr[x][y] == '-':
                    start[y], start[y+1] = start[y+1], start[y]
    
    # 중간 결과
    # print(start)

    for x in reversed(range(question_line+1, n)):
        if arr[x][0] == '?':
            break
        else:
            for y in range(k-1):
                if arr[x][y] == '-':
                    dest[y], dest[y+1] = dest[y+1], dest[y]

    # ? 아래의 결과
    # print(dest)

    # 두개의 결과를 비교
    for idx in range(k-1):
        if start[idx] == dest[idx]: 
            answer.append("*")
        else:
            if start[idx] == dest[idx+1]:
                answer.append("-")
            elif idx != 0 and start[idx] == dest[idx-1]:
                answer.append("*")
            else:
                return(''.join(['x' for _ in range(k-1)]))
    
    return ''.join(answer)

if __name__ == "__main__":
    k = int(input())
    n = int(input())
    dest = list(input())
    
    arr = []
    for _ in range(n):
        arr.append(list(sys.stdin.readline().rstrip()))
    
    ret = solution()
    print(ret)
    