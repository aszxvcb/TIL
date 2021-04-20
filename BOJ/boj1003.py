'''
    factorial dp구현에서 배열에 결과값 대신 f(0), f(1)의 호출갯수를 저장
    f(0) = 1 0
    f(1) = 0 1
    으로 초기값 세팅
    f(2) = f(0) + f(1) = [1,0] + [0,1] = [1,1]
    f(3) = f(1) + f(2) = [0,1] + [1,1] = [1,2]
    ...
'''
global factorial

def solution(n):
    global factorial
    
    for idx in range(2,n+1):
        elem = list(sum(i) for i in zip(factorial[idx-1], factorial[idx-2]))
        factorial.append(elem)
    
    return factorial[n]

if __name__ == "__main__":
    global factorial

    N = int(input())
    for _ in range(N):
        factorial = [[1,0], [0,1]]
        ret = solution(int(input()))
        print(ret[0], ret[1])