'''
    stack을 사용해야겠다고 바로 생각못했던 문제

    stack 두개를 이용하여 풀이
    stack, out 두개를 만들고
    stack에 새로 들어오는 값과 top 과 비교하여 크다면
    out으로 저장. 
    이때 idx, val 두개를 잘 저장해놓고
    최종적으로 idx를 기준으로 정렬해서 순서대로 출력할 수 있게끔

    풀고난 후
    idx를 기준으로 정렬할 필요없이,
    answer[N] 을 미리 만들어놓고
    answer[idx] = val
    바로 넣어줄 수 있다
    random Access가 가능하니깐
'''

def solution(arr):
    stack = []
    NGE = [0] * len(arr)
    
    # arr의 idx, num 을 이용
    for idx, num in enumerate(arr):
        if len(stack) == 0 :
            stack.append((num,idx))
        else:
            # top과 비교해서 NGE 찾기
            while len(stack) > 0 and stack[-1][0] < num:
                NGE[stack[-1][1]] = num
                stack.pop()
            
            # 새로 들어온 숫자 추가
            stack.append((num,idx))

    # 남은 숫자들 처리
    for num, idx in stack:
        NGE[idx] = -1
    
    return NGE


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    ret = solution(arr)

    print(" ".join(list(map(str, ret))))