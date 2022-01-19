'''
    전체 가로등을 맵으로 저장하여, 균형잡힌 가로등 존재여부를 빠르게 체크

    입력되는 가로등의 순서가 의미가 있음.. 입력되는 순서대로 순회하여 균형여부 체크
'''

import sys

def solution(arr):
    dic = {}
    for elem in arr:
        if elem[0] not in dic.keys(): # 딕셔너리 초기화
            dic[elem[0]] = {}
    
        dic[elem[0]][elem[1]] = 1
        
    # print(dic)

    for i in range(0,len(arr)-1):
        A = arr[i]
        B = arr[i+1]
        # print(A[0], B[1], B[0], A[1])
        try:
            if dic[A[0]][B[1]] == 1 and dic[B[0]][A[1]] == 1:
                pass
        except KeyError:
            print("NOT BALANCED")
            return

    else:
        print("BALANCED")
        return


if __name__ == "__main__":
    TC = int(input())
    
    for _ in range(TC):
        num = int(input())
        arr = []
        for _ in range(num):
            arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

        solution(arr)