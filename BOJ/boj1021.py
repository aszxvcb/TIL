'''
    rotate를 어느방향으로 할지 결정하는 것이 문제
    정방향으로 회전할때와, 역방향으로 회전할때의 횟수를 구한 후,
    작은 값으로 결정
'''

from collections import deque
from time import sleep

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr = deque(arr)
cnt = 0
idx_arr = deque([ idx+1 for idx in range(N) ])
# print(idx_arr)

while( len(arr) > 0 ):
    if idx_arr[0] == arr[0]:
        idx_arr.popleft()
        arr.popleft()
    else:
        target_index = idx_arr.index(arr[0])
        # print(target_index , len(idx_arr)-target_index)
        if target_index < len(idx_arr)-target_index:
            cnt += target_index
            idx_arr.rotate(-target_index)
        else:
            cnt += len(idx_arr)-target_index
            idx_arr.rotate((len(idx_arr)-target_index))

    # print(idx_arr, arr)
    # sleep(1)

print(cnt)
    
