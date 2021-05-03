'''
    페이지 교체 알고리즘 OPT 방식
    OPT : https://velog.io/@qweadzs/BOJ-1700-%EB%A9%80%ED%8B%B0%ED%83%AD-%EC%8A%A4%EC%BC%80%EC%A4%84%EB%A7%81Python 

    멀티탭을 모두 사용하고 있을 때, 어떤 코드를 뽑을 것인지 선택하는 문제
    - 앞으로 다시 사용하지 않을 코드
    위 조건을 만족하는 코드가 없다면
    - 가장 나중에 다시 사용할 코드
    먼저 사용할 것을 빼버리면, 다시 사용할 때 다시 꽂아야 함.
'''

from collections import deque

def solution(N, arr):
    use = []
    cnt = 0

    while(len(arr) > 0):
        # print(use ,arr)
        # 이미 사용하고 있다면 건너뜀
        if arr[0] in use:
            arr.popleft()
        else:
            if len(use) < N:
                use.append(arr.popleft())
            # 사용하고 있지 않다면, 하나를 뽑아야함
            else:
                max_idx = -1
                for idx, item in enumerate(use): 
                    # 앞으로 사용하지 않을 것
                    if item not in arr:
                        use[idx] = arr.popleft()
                        cnt += 1
                        break
                    # 가장 나중에 사용할 것
                    else:
                        new_idx = arr.index(item)
                        if new_idx > max_idx:
                            max_idx = new_idx
                            max_item = item
                else:
                    use[use.index(max_item)] = arr.popleft()
                    cnt += 1
    # print(use ,arr)
    print(cnt)

if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = deque(list(map(int, input().split())))

    solution(N, arr)