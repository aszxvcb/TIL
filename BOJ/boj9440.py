'''
    합이 가장 작은 수를 만들기 위해서는
    더하는 두 숫자의 자릿 수가 비슷해야함

    주어진 숫자들을 정렬 후
    자릿수가 비슷한 가장 작은 두수 만들기
    각 자리수의 합이 가장 작은 값을 가지는 수
    0은 맨앞에 올 수 없음 -> 첫자리를 0이 아닌 수로 만들어준다.
'''

import sys
from collections import deque

def solution(size, arr):
    arr.sort()
    arr = deque(arr)
    leftNum = deque([])
    rightNum = deque([])
    
    if size % 2 == 1:
        leftNum.append(arr.popleft())

    for _ in range(size//2):
        if len(leftNum) > 0 and leftNum[0] == '0':
            leftNum.appendleft(arr.popleft())
        else:
            leftNum.append(arr.popleft())
        
        if len(rightNum) > 0 and rightNum[0] == '0':
            rightNum.appendleft(arr.popleft())
        else:
            rightNum.append(arr.popleft())
    
    # print(arr)

    leftNum = int("".join(leftNum))
    rightNum = int("".join(rightNum))

    # print(leftNum)
    # print(rightNum)

    return leftNum+rightNum

if __name__ == "__main__":
    
    while( True ):
        line = sys.stdin.readline().rstrip()
        
        if line == '0':
            break
        else:
            line = line.split()
            size = line[0]
            arr = line[1:]

            ret = solution(int(size), arr)
            print(ret)