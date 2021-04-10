'''
visit 배열을 이용하여 풀이
=> 시간초과 발생

def solution(X, A):
    answer = -1

    visit = [ False for _ in range(X)]
    
    for idx in range(len(A)):
        visit[A[idx]-1] = True
        if False not in visit:
            return idx
    else:
        return -1
'''

'''
    set을 이용하여 중복을 제거하고
    set의 원소의 갯수를 확인하여 문제 해결
'''

def solution(X, A):
    answer = -1

    leaves_set = set()
    
    for idx in range(len(A)):
        leaves_set.add(A[idx])
        if len(leaves_set) == X:
            return idx
    else:
        return -1
