'''
    걸린시간 : 1시간 이상

    접근방법
    1. R이 연속으로 2번이 나오면 뒤집지 않아도 된다
    2. R에 따라 D의 위치가 바뀌므로 함수 실행 순서는 지켜야한다
    => 함수를 stack에 넣어 R이 연속으로 나오는 걸 처리해주자!
    결과 : 시간초과 // 함수의 갯수 N 만큼 순회를 해야하기 때문에 비효율적
    해결 : D를 만날때까지의 R의 갯수를 세어서, 짝수면 앞에서 홀수면 뒤에서 제거

    3. D 연산을 list slice로 하자
    4. D 의 갯수를 세어 한번에 list slice 하면 어떨까
    결과 : 시간초과 // slice의 평균 비용이 결코 작지 않음
    해결 : Deque 사용해서 D를 만날때마다 하나씩 제거

    5. 빈배열의 경우 에러를 출력하자
    결과 : 틀렸습니다.
    해결 : error의 출력조건은 빈배열이 아니라, 빈배열에 D연산을 하는 경우임.
    문제를 잘 읽어야 함

    입출력 파싱하는 것도 까다로웠던 문제
'''

from collections import deque

def solution(func, arr):
    R_flag = False
    
    arr = deque(arr)
    for f in func:
        if f == 'R':
            R_flag = not R_flag
        elif f == 'D':
            if len(arr) == 0:
                return "error"
            if R_flag == False:
                arr.popleft()
            else:
                arr.pop()

    if R_flag == False:
        return arr
    else :
        arr.reverse()
        return arr


if __name__ == "__main__":
    T = int(input())
    
    for _ in range(T):
        func = input()
        input()
        temp = input()[1:-1]
        
        if ',' in temp:
            arr = temp.split(',')
        elif len(temp) == 0:
            arr = []
        else:
            arr = [temp]

        ret = solution(func, arr)

        if "error" not in ret:
            string = ",".join(ret)
            print("[{}]" .format(string))
        else:
            print("error")
    