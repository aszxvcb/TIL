'''
    중위표현식 -> 후위표현식

    1. 연산자별로 우선순위를 부여한다.
    2. 중위표현식을 앞에서부터 탐색한다.
    3. 피연산자는 출력하고, 연산자는 stack에 넣는다
    4. 스택에 이전 연산자보다 우선순위가 작은 것이 온다면, 연산자를 스택에서 출력(pop)한다.
    
'''

def solution(data):
    
    priority = {'+':1 , '-':1, '*':2, '/':2, '(':0, ')':0}
    arr = []
    stack = []
    for elem in data:
        # print(stack, elem)
        if elem.isalpha():
            arr.append(elem)
        elif elem == '(':
            stack.append(elem)
        elif elem == ')':
            while len(stack) > 0 and stack[-1] != '(':
                arr.append(stack.pop())
            if len(stack) > 0:
                stack.pop()
        else:
            # 우선순위에 따라 연산자를 출력
            while(len(stack)>0 and priority[stack[-1]] >= priority[elem]):
                arr.append(stack.pop())    
            stack.append(elem)
    # 스택에 남은 연산자들을 출력
    else:
        while(len(stack)>0):
            arr.append(stack.pop())

    # print(arr)
    return ''.join(arr)

if __name__ == "__main__":
    data = list(input())
    ret = solution(data)

    print(ret)