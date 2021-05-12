'''
    수학적으로 접근하면 쉽게 풀수 있는 문제
'''

def solution(arr, B, C):
    answer = 0

    for student in arr:
        if student - B <= 0:
            answer += 1
        elif (student - B) % C > 0 :
            answer += (student-B) // C + 2
        else :
            answer += (student-B) // C + 1

    print(answer)


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    B, C = map(int, input().split())

    solution(arr, B, C)
