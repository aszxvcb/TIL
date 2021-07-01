'''
    스택을 이용한 풀이
    bomb의 뒤에서 조건을 체크했다.
'''

def solution(s, bomb):
    stack = []

    for elem in s:
        stack.append(elem)
        
        if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
            for i in range(1, len(bomb)+1):
                if stack[-i] != bomb[-i]:
                    break
            else:
                for _ in range(len(bomb)):
                    stack.pop()

    if len(stack) != 0:
        print(''.join(stack))
    else:
        print("FRULA")

if __name__ == "__main__":
    s = input()
    bomb = input()

    solution(s, bomb)