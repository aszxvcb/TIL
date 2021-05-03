'''
    SJF
    걸리는 시간이 짧은 것부터 처리
'''


def solution(arr):
    answer = 0
    sum_time = 0

    arr.sort()
    # print(arr)
    
    for time in arr:
        sum_time = sum_time + time
        answer += sum_time
        # print(sum_time)
    
    # print(answer)
    return answer


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int,input().split()))

    ret = solution(arr)
    print(ret)
