'''
    BFS. 메모리초과가 나는데, 중복체크 횟수를 줄이는 로직이 필요함
    방문한 배열의 좌표에 0을 넣어 방문 체크를 실시
    queue에 값을 넣을 때, 표시를 하여 동일한 좌표가 다시 큐에 들어가지 않도록 방지
'''


from collections import deque
from copy import deepcopy

def solution(originArr, colorFlag):
    arr = deepcopy(originArr)
    size = len(arr)
    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]

    queue = deque()
    # visit = [ [ False for _ in range(size)] for _ in range(size) ]
    ret = 0

    for x in range(size):
        for y in range(size):
            if arr[x][y] == 0: # 방문을 했던 부분이라면 패스
                continue

            color = arr[x][y]
            queue.append([x,y])
            ret = ret+1
            
            while(queue):
                i, j = queue.popleft()
                arr[i][j] = 0

                for idx in range(4):
                    nx = i + dx[idx]
                    ny = j + dy[idx]

                    if not (0 <= nx and nx < size and 0 <= ny and ny < size):
                        continue

                    if colorFlag == "general":
                        if arr[nx][ny] != 0 and arr[nx][ny] == color : # 방문하지 않았고, 컬러가 같다면. 큐에 삽입
                            queue.append([nx,ny])
                            arr[nx][ny] = 0
                    
                    elif colorFlag == "blind":
                        if color in ['R', 'G']:
                            if arr[nx][ny] != 0 and arr[nx][ny] in ['R','G']:
                                queue.append([nx,ny])
                                arr[nx][ny] = 0
                        else:
                            if arr[nx][ny] != 0 and arr[nx][ny] == color :
                                queue.append([nx,ny])
                                arr[nx][ny] = 0

    return ret

if __name__ == "__main__":
    TC = int(input())

    arr = []
    for _ in range(TC):
        arr.append(list(input()))
    
    result = [solution(arr,"general"), solution(arr,"blind")]
    print(result[0], result[1])