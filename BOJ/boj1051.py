'''
    20분 소요
    모든 경우의 수 탐색
    현재 찾은 최대길이 보다 작으면 탐색 안함
'''

import sys

def solution(arr):
    max_line_len = 0

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            for length in range(max_line_len,50):
                ru = [i, j+length]
                ld = [i+length, j]
                rd = [i+length, j+length]

                if ru[1] < M and ld[0] < N and rd[0] < N and rd[1] < M:

                    num = arr[i][j]
                    if arr[ru[0]][ru[1]] == num and arr[ld[0]][ld[1]] == num and arr[rd[0]][rd[1]] == num:
                        # print([i,j], ru, ld, rd)
                        max_line_len = length
                else:
                    break

    return max_line_len
                

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, list(sys.stdin.readline().rstrip()))))
    
    # for line in arr:
    #     print(line)

    ret = solution(arr)
    print(pow(ret+1,2))
