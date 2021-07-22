'''
    - 스택

    입력받은 순서에서 선택할 수 있는 것은 아래 두가지 경우이다.
        - 다음 순서에 나올 값
        - 스택의 마지막의 값

    - 테스트케이스
    5
    5 4 2 1 3
    
    Nice
'''
def solution(arr):
    size = len(arr)
    stack = []
    cur_num = 1
    i = 0

    while( i != size ):
        # 원래 줄의 다음 순서
        if arr[i] == cur_num:
            cur_num += 1
        # 최근 스택으로 옮겨진 순서
        elif stack and stack[-1] == cur_num:
            stack.pop()
            i -= 1
            cur_num += 1
        # 순서가 안된다면 스택에 저장
        else:
            stack.append(arr[i])
        i += 1

    while(stack):
        if stack.pop() == cur_num:
            cur_num += 1
            continue
        else:
            print("Sad")
            return
    else:
        if cur_num-1 == size:
            print("Nice")

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    solution(arr)