'''
    리스트의 원소를 쉬프트하는 문제
    K의 갯수를 A의 원소 갯수만큼 나누면
    연산횟수를 줄일 수 있음

    A가 비어있을때를 처리하지 않아, 감점이 있었던 문제
'''

def solution(A, K):
    answer = A

    if len(A) == 0 :
        return A
    
    # 원소 개수만큼 K를 나눈 나머지를 구해야함
    K = K % len(A)

    # 쉬프트
    for _ in range(0,K):
        temp = []
        temp.append(answer[-1])
        temp.extend(answer[0:-1])
        answer = temp
        # print(answer)

    return answer
