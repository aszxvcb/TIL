'''
    분할정복 / 재귀 문제
    
    왼쪽 위/아래, 오른쪽 위/아래. 4군데로 나눠서 재귀적으로 처리한다.
    부분을 나누는것이 조금 헷갈렸던 문제
'''

import sys

def solution(arr):
    global answer
    # print(answer)
    answer.append('(')

    size = len(arr[0])
    part = [[],[],[],[]]

    # 재귀 탈출 조건. 가로/세로 사이즈가 1이라면 더이상 압축이 되지 않음
    if size == 1:
        answer.append(arr[0][0])
    # 압축이 가능한 상태라면
    else:
        for i in range(size):
            if i < size // 2 :
                #왼쪽위
                part[0].append(arr[i][0:size//2])
                #오른쪽위
                part[1].append(arr[i][size//2:])
            else:
                #왼쪽아래
                part[2].append(arr[i][0:size//2])
                #오른쪽아래
                part[3].append(arr[i][size//2:])

        # for p in part:
        #     for line in p:
        #         print(line)
        #     print("="*10)

        cnt = [0] * 4 # 왼쪽위,오른쪽위,왼쪽아래,오른쪽아래
        for i in range( size//2 ):
            cnt[0] += part[0][i].count(1)
            cnt[1] += part[1][i].count(1)
            cnt[2] += part[2][i].count(1)
            cnt[3] += part[3][i].count(1)

        # print(cnt)

        # 원소를 확인
        for i in range( 4 ):
            if cnt[i] == 0:
                answer.append("0")
            elif cnt[i] == (size//2)**2:
                answer.append("1")
            else:
                solution(part[i])

    answer.append(')')    


if __name__ == "__main__":
    answer = []
    N = int(input())
    
    arr = []
    for _ in range(N):
        line = list(map(int, sys.stdin.readline().rstrip()))
        arr.append(line)

    # for line in arr:
    #     print(line)

    # 모든 원소를 확인
    all_cnt = 0
    size = len(arr[0])
    for i in range(size):
        all_cnt += arr[i].count(1)

    if all_cnt == 0:
        answer.append("0")
    elif all_cnt == size ** 2:
        answer.append("1")
    # 한번에 압축이 되지 않는다면 재귀적으로 처리
    else :
        solution(arr)
    
    print("".join(answer))
