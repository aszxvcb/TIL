'''
    BFS로 풀이
    방향이 상하좌우 4개가 아닌, 대각선포함 8개
    구현문제
'''

def solution(N, board , click):

    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    ret = [[ '.' for _ in range(N)] for _ in range (N)]
    flag = False

    for i in range(N):
        for j in range(N):
            num = 0
            if click[i][j] == 'x':  # 클릭한 점들만 체크
                if board[i][j] == '*' : # 클릭한 점이 지뢰라면 flag
                    flag = True

                for d in range(8):
                    nx = i+dx[d]
                    ny = j+dy[d]
                    # print(i, j, nx, ny)
                    if 0 <= nx and nx < N and 0 <= ny and ny < N:
                        if board[nx][ny] == '*':
                            num += 1
                ret[i][j] = str(num)


    if flag == True:
        for i in range(N):
            for j in range(N):
                if board[i][j] == '*':
                    ret[i][j] = '*'

    return ret


if __name__ == "__main__":

    N = int(input())
    board = []
    click = []


    for _ in range(N):
        board.append(list(input()))
    for _ in range(N):
        click.append(list(input()))

    # for i in range(len(board)):
    #     print(board[i])
    # for j in range(len(board)):
    #     print(click[j])    

    ret = solution(N, board, click)

    for i in range(N):
        print( ''.join(ret[i] ))

