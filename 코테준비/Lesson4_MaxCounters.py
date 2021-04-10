'''
    정확도는 맞지만 시간초과 발생

def solution(N, A):
    answer = [0] * N

    for num in A:
        if 1 <= num and num <= N:
            answer[num-1] += 1
        elif num == N+1:
            answer = [max(answer)] * N

    return answer
'''

'''
    시간복잡도가 O(N+M)으로 좋아졌지만,
    아직도 최대사이즈에서는 시간초과 발생

    def solution(N, A):
    answer = [0] * N
    max_num = 0
    for num in A:
        if 1 <= num and num <= N:
            answer[num-1] += 1
            if max_num < answer[num-1]:
                max_num = answer[num-1]
        elif num == N+1:
            answer = [max_num] * N

    return answer
'''

