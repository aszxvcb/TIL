'''
    stack을 두개 사용하여 문제 해결, 구현 문제
    재귀로 시도하려고했으나, 계산결과를 다루기가 어려울 것 같았음

    stack을 한번 빠르게 돌려서 에러 먼저 체크하는게 
    코드상으로 깔끔해보일수도 있을 것 같음
'''

def solution(string):
    stack = []      # 입력을 stack에 쌓음
    num_stack = []  # 괄호안에 생기는 숫자를 계산하기 위한 스택
    brakets = ['(',')','[',']']
    
    for s in string:
        # 일반적인 여는 괄호는 stack에 삽입
        if s == '(' or s == '[': 
            stack.append(s)
        # 닫는 괄호의 경우
        elif s == ')':
            # 잘못된 괄호 에러
            if len(stack) == 0:
                return 0

            for i in reversed(stack):
                # 여는 괄호가 나올때까지 뒤에서부터 체크
                if i != '(':
                    # 짝이 안맞는 괄호가 나오면 에러
                    if i in brakets:
                        return 0
                    # 탐색 중 나오는 숫자는 num_stack에 삽입
                    num_stack.append(int(i))
                    stack.pop()
                # 여는 괄호가 나왔다면
                else:
                    stack.pop()
                    # 내부에 덧셈해줄 숫자가 없다면 2 삽입
                    if len(num_stack) == 0:
                        stack.append(2)
                    # 있다면 덧셈 계산
                    else:
                        num = sum(num_stack)
                        num_stack.clear()
                        stack.append(2*num)
                    break
        elif s == ']':
            if len(stack) == 0:
                return 0
            for i in reversed(stack):
                if i != '[':
                    if i in brakets:
                        return 0
                    num_stack.append(int(i))
                    stack.pop()
                else:
                    stack.pop()
                    if len(num_stack) == 0:
                        stack.append(3)
                    else:
                        num = sum(num_stack)
                        num_stack.clear()
                        stack.append(3*num)
                    break
        # print(stack)

    for braket in brakets:
        if braket in stack:
            return 0
    else:
        return sum(stack)


if __name__ == "__main__":
    string = input()
    ret = solution(string)
    print(ret)