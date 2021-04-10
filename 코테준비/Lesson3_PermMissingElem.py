'''
    문제를 제대로 확인하지 못해 감점.
    코딜리티의 경우, assumptions 을 제대로 보고 예측가능한 테스트케이스를 확인해보자..

    1~N 사이에 없는 숫자를 찾는 문제
    라고만 생각하여 패스하지 못하는 테스트케이스가 있었음
    1~N 까지 모든 수가 존재한다면, N+1을 리턴해야함
'''

def solution(A):
    answer = -1

    # N이 0일 때
    if len(A) == 0:
        return 1

    A.sort()
    num = 1
    for i in A:
        if i == num:
            num += 1
        else :
            answer = num
            break
    else:   # 모든 수가 존재한다면
        answer = num

    return answer

if __name__ == "__main__":
    ret = solution([2,1])
    print(ret)