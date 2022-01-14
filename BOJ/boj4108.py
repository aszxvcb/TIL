from copy import deepcopy

def solution(arr):

    ret = deepcopy(arr)

    # for x in ret:
    #     print(x)

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    for x in range(len(arr)):
        for y in range(len(arr[0])):
            
            if arr[x][y] == '.':
                num = 0
                for i in range(len(dx)):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if nx >= 0 and nx < len(arr) and ny >= 0 and ny < len(arr[0]):
                        if arr[nx][ny] == '*':
                            num = num + 1
                
                ret[x][y] = str(num)

    for x in ret:
        print("".join(x))
        

if __name__ == "__main__":
    while(True):
        arr = []
        R, C = map(int, input().split())

        if R == 0 and C == 0:
            exit()

        for _ in range(R):
            arr.append(list(input()))

        # for x in arr:
        #     print(x)

        solution(arr)