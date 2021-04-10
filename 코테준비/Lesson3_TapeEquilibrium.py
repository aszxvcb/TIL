'''
    # 첫번째 풀이
    문제에 주어진대로 그대로 풀이하였을 경우, 시간초과 발생

def solution(A):
    answer = []
    
    for P in range(1,len(A)):
        left = 0
        right = 0
        for num in A[0:P]:
            left += num
        for num in A[P:]:
            right += num

        answer.append(abs(left-right))  
    return min(answer)
'''

'''
    # 두번째 풀이
    1) set 을 이용해서 중복된 값을 지워 줌
    2) left, right를 계산할 때, 이전 계산결과에 경계값만 연산하여 계산
    => 시간 초과

    def solution(A):
    answer = []
    answer_set = set()
    
    left = 0
    right = sum(A,0)

    for P in range(1,len(A)):
        left += A[P-1]
        right -= A[P-1]
    
        answer_set.add(abs(left-right))  
        answer = min(list(answer_set))
    
    return answer

''' 

'''
    # 세번째 풀이
    최소값을 계속 갱신
'''
    def solution(A):
    answer = float('inf')
    
    left = 0
    right = sum(A,0)

    for P in range(1,len(A)):
        left += A[P-1]
        right -= A[P-1]
    
        calc = abs(left-right)
        if answer > calc:
            answer = calc
    
    return answer