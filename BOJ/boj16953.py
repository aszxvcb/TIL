from collections import deque
from time import sleep

def append_one(num):
    return int(str(num) + '1')

def solution(num, target):
    queue = deque()
    
    queue.append([num, 0])
    
    while(queue):
        cur_num, cur_cnt = queue.popleft()

        if cur_num == target:
            return cur_cnt + 1

        # 두배한 값 삽입
        if cur_num * 2 <= target:
            queue.append([cur_num * 2, cur_cnt+1])
        
        # 마지막에 1을 붙인 삽입
        if append_one(cur_num) <= target:
            queue.append([append_one(cur_num), cur_cnt+1])

    else:
        return -1


if __name__ == "__main__":
    num, target = list(map(int, input().split()))

    ret = solution(num, target)
    print(ret)