"""
    작은 기능부터 하나씩 정의하고 구현 (Bottom-Up)
    for-loop을 많이 돌아야하는 이 같은 문제는 for문을 먼저 만들기전에
    하나의 경우를 정의해놓고, 기능부터 구현하는 것이 접근하기 쉽다.

    문제 접근은 
    완전탐색으로 접근하되, 
    구슬의 갯수만큼 재귀호출,
    폭탄의 연쇄작용을 위해서는 BFS,
    중력을 적용하기 위해서는 Queue 를 사용.
    => 구현하기 까다로웠다...

    상하좌우를
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    과 같이 delta를 정의하고
    delta * range 를 이용해서 범위를 늘려가는 것도 간결하게 짤 수 있는 방법이 된다.

    블럭을 내리는 것은 아래에서 위로 탐색하면서 블럭을 큐에 담고
    다시 아래에서부터 큐에서 빼내고, 큐가 비면 나머지는 빈 공간으로 넣어주면 된다.


    !!!
    파이썬에 배열을 넘길때는 얕은복사가 일어남.
    import copy
    copy.deepcopy(복사할배열)
    을 이용해서 깊은 복사가 필요함

    파이썬에서의 객체들은 mutable과 immutable로 나누어진다
    list, set은 mutable  /  str은 immutable
    immutable 의 경우 수정하게되면 재할당이 일어남 -> 새로운 id를 가짐
    반면에, mutable 객체들은 참조하고 있는 값을 바꿈 -> 같은 id를 가짐
    때문에 대입 후 수정시에 같은 아이디를 가진 다른 변수에서도 원치않는 변화가 생길 수 있음.

    참고 : https://velog.io/@aonee/Python-%EC%9E%90%EB%A3%8C%ED%98%95%EC%9D%98-%EA%B0%92-%EC%A0%80%EC%9E%A5-%EB%B3%B5%EC%82%AC-copy
"""

from collections import deque
from time import sleep
import copy

global  W, H, N, min_cnt, min_arr

def solution(input_arr, n):
    global W,H,N
    for i in range(W):
        arr = copy.deepcopy(input_arr)
        '''맨위 찾기'''
        top = 0
        power = arr[top][i]
        for h in reversed(range(H)):
            # print( arr[h][i] )
            if arr[h][i] == 0 and h+1 < H:
                top = h+1
                power = arr[top][i]
                break
        # print(top)

        '''범위의 폭탄이 한꺼번에 터짐.'''
        bomb_queue = deque([[top, i, power]])
        # print(bomb_queue)
        while( len(bomb_queue) > 0 ):
            '''중앙'''
            x,y,p = bomb_queue.popleft()
            arr[x][y] = -1
            '''좌'''
            for dy in range(1, p):
                if y-dy < 0:  # 범위를 벗어나면 스킵
                    break
                if arr[x][y-dy] > 1:
                    # print("L ", x,y-dy,arr[x][y-dy])
                    bomb_queue.append([x,y-dy,arr[x][y-dy]])
                    arr[x][y-dy] = -1
                elif arr[x][y-dy] == 1:
                    arr[x][y-dy] = -1 
            '''우'''
            for dy in range(1, p):
                if y+dy >= W:
                    break
                if arr[x][y+dy] > 1:
                    # print("R ",x,y+dy,arr[x][y+dy])
                    bomb_queue.append([x,y+dy,arr[x][y+dy]])
                    arr[x][y+dy] = -1
                elif arr[x][y+dy] == 1:
                    arr[x][y+dy] = -1
            '''상'''
            for dx in range(1,p):
                if x-dx < 0:
                    break
                if arr[x-dx][y] > 1:
                    # print("U ", x-dx,y,arr[x-dx][y])
                    bomb_queue.append([x-dx,y,arr[x-dx][y]])
                    arr[x-dx][y] = -1
                if arr[x-dx][y] == 1:
                    arr[x-dx][y] = -1
            '''하'''
            for dx in range(1,p):
                if x+dx >= H:
                    break
                if arr[x+dx][y] > 1:
                    # print("D ", x+dx,y,arr[x+dx][y])
                    bomb_queue.append([x+dx,y,arr[x+dx][y]])
                    arr[x+dx][y] = -1
                elif arr[x+dx][y] == 1:
                    arr[x+dx][y] = -1
                
        # for h in range(H):
        #     print(arr[h])
        # print()

        '''빈 사이를 메꾼다. 동시에 블록의 수를 센다'''
        for w in range(W):
            queue = deque()
            for h in reversed(range(H)):
                if arr[h][w] not in [0,-1]:
                    queue.append(arr[h][w])
            for h in reversed(range(H)):
                if len(queue) != 0:
                    arr[h][w] = queue.popleft()
                else:
                    arr[h][w] = 0
        
        # for h in range(H):
        #     print(arr[h])

        '''N 만큼 재귀호출'''
        if n < N-1:
            temp = copy.deepcopy(arr)
            solution(temp,n+1)
        elif n == N-1:
            # for line in arr:
            #     print(line)
            # print()
            count_block(arr)

    return 

''' arr에서 블럭의 갯수를 계산 '''
def count_block(arr):
    # for line in arr:
    #     print(line)
    # print()
    global W, H, min_cnt, min_arr
    cnt = 0
    for i in range(H):
        for j in range(W):
            if(arr[i][j] != 0):
                cnt += 1
    if min_cnt > cnt:
        min_cnt = cnt
        min_arr = copy.deepcopy(arr)

if __name__ == "__main__":
    global W, H, N, min_cnt, min_arr

    T = int(input())
    for t in range(T):
        min_cnt = float('INF')
        min_arr = [[]]
        N,W,H = map(int, input().split(" "))

        arr = [] 
        for _ in range(H):
            line = list(map(int, input().split()))
            arr.append(line)

        # for h in range(H):
        #     print(arr[h])

        solution(arr,0)

        # print('=' * 10)
        # print(min_cnt)
        # for line in min_arr:
        #     print(line)

        print("#{} {}".format(t+1, min_cnt))
        # for line in min_arr:
        #     print(line)
