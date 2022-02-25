# 문자열 압축
'''
    1. 문자열을 적당한 갯수로 나눈다.
    2. 스택을 이용하여 카운트 한다.
'''

def solution(s):
    min_size = float('INF')

    if len(s) == 1:
        return 1
    
    ## 문자열을 몇개씩 자를 것인지
    for split_size in range(1, len(s)):
        result = []
        stack = []
        size = 0
        chunk = [ s[i : i+split_size] for i in range(0, len(s), split_size) ]
        
        for elem in chunk:
            if len(stack) == 0: # 스택 초기설정
                stack.append(elem)
                size = 1
            else:
                if stack[-1] == elem: # 같은 문자가 온다면
                    size = size+1
                else:                 # 다른 문자가 온다면
                    if size != 1:
                        result.append(str(size))
                    result.append(stack.pop())

                    stack = [elem]
                    size = 1
        else:   # 루프가 끝나면 스택 비워주기
            if size != 1:
                result.append(str(size))
            result.extend(stack)

        # 최소길이 갱신
        result = "".join(result)
        if len(result) < min_size:
            min_size = len(result)
                
    # print(min_size)
    return min_size

if __name__ == "__main__":

    s = "a"
    result = 1
    assert solution(s) == result

    #TC1
    s = "aabbaccc"
    result = 7
    assert solution(s) == result
    
    #TC2
    s = "ababcdcdababcdcd"
    result = 9
    assert solution(s) == result

    #TC3
    s = "abcabcdede"
    result = 8
    assert solution(s) == result

    #TC4
    s = "abcabcabcabcdededededede"
    result = 14
    assert solution(s) == result

    #TC5
    s = "xababcdcdababcdcd"
    result = 17
    assert solution(s) == result