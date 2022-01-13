'''
    입력된 리스트를 L, R로 구분해서 하나로 연결한 후,
    전체 리스트를 순회하며, 먼저지나간 차의 시간을 확인하여 지워준다.
    L일 경우 카운트하여 왼쪽에서 지나간 차의 수를 카운트한다.
'''

from collections import deque

def solution(left, right):

    left = list(map(lambda x: (x,'L'), left))
    right = list(map(lambda x: (x, 'R'), right))

    # print(left)
    # print(right)
    
    ## 하나로 모아서 정렬
    arr = []
    arr.extend(left)
    arr.extend(right)
    arr.sort()

    ## deque
    queue = deque(arr)
    ret = 0
    # print(queue)
    while( queue ):
        # print("check ", queue[0])
        num, direction = queue.popleft()
        
        if direction == 'L':
            ret = ret + 1
            rev_direction = 'R'
        else :
            rev_direction = 'L'

        for j in reversed(range(len(queue))):
            if ((queue[j][0] == num + 500) and (queue[j][1] == direction)) or \
                ((queue[j][0] == num + 1000) and (queue[j][1] == rev_direction)) or \
                ((queue[j][0] == num + 1500) and (queue[j][1] == rev_direction)):
                    queue.remove(queue[j])

        # print(queue)

    return ret


if __name__ == "__main__":
    TC = int(input())

    for _ in range(TC):
        N = int(input())
        left = list(map(int, input().split()))
        right = list(map(int, input().split()))

        ret = solution(left, right)
        print(ret)

    
