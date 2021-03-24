''' 
    stack을 만들어서 마지막 두 원소가 같다면 터트려주는 방식
'''

def solution(board, moves):
    answer = 0
    num = 0
    stack = list()

    for col in moves:
        for row in range(0, len(board)):
            if board[row][col-1] != 0:
                print(row, col-1, board[row][col-1])
                if( len(stack) != 0 and stack[-1] == board[row][col-1] ):
                    stack.pop(-1)
                    num = num + 2
                else:
                    stack.append(board[row][col-1])
                board[row][col-1] = 0
                break

    # for elem in stack:
    #     print( elem , end = '')
    # print()

    answer = num
    return answer


if __name__ == "__main__":
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    ret = solution(board, moves)
    print(ret)