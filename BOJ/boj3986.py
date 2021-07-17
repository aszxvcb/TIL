'''
    stack을 이용하여 같은 두 문자가 만나는지 체크
    입력 받은 문자열이 조건을 만족하면 좋은 단어
'''

import sys

def solution(string):
    stack = []

    for i in range(len(string)):
        # print(stack)
        if len(stack) >= 1 and stack[-1] == string[i]:
                stack.pop()
        else:
            stack.append(string[i])

    # print(stack)
    
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    N = int(input())
    
    arr = []
    cnt = 0
    for _ in range(N):
        string = sys.stdin.readline().rstrip()
        
        if solution(string) == True:
            cnt += 1

    print(cnt)
