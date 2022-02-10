'''
좌표 계산을 잘해야하는 문제
x,y / row, col / UP,DOWN,LEFT,RIGHT
등을 잘 계산해야함. 왼쪽 상단을 (0,0)으로 놓고 계산함

각 방향에 따라 어느 공을 먼저 움직일 것인가를 체크해야함

7 7
#######
#..R#B#
#.#####
#.....#
#####.#
#O....#
#######

5 5
#####
#OBR#
#####
#####
#####

4 4
####
#.R#
#OB#
####

7 7
#######
#...O.#
#.....#
#.....#
#.B...#
#..R..#
#######
'''
from collections import deque
from copy import deepcopy

def setOrder(red, blue, dir):
    order = []
    
    if dir == "L":
        if red[1] < blue[1]:
            order.append("red")
            order.append("blue")
        else:
            order.append("blue")
            order.append("red")
    elif dir == "D":
        if red[0] > blue[0]:
            order.append("red")
            order.append("blue")
        else:
            order.append("blue")
            order.append("red")
    elif dir == "U":
        if red[0] < blue[0]:
            order.append("red")
            order.append("blue")
        else:
            order.append("blue")
            order.append("red")
    elif dir == "R":
        if red[1] > blue[1]:
            order.append("red")
            order.append("blue")
        else:
            order.append("blue")
            order.append("red")

    # print(order)
    return order

if __name__ == "__main__":
    
    row, col = map(int, input().split())
    board = []
    red = None
    blue = None
    hole = None

    for col in range(row):
        line = list(input())
        board.append(line)

        if 'R' in line:
            red = [col, line.index('R')]
        
        if 'B' in line:
            blue = [col, line.index('B')]
        
        if 'O' in line:
            hole = [col, line.index('O')]

    # for line in board:
        # print(line)
    # print("R : ", red, "B : ", blue, "H : ", hole)

    dx = [0, 1, -1, 0]
    dy = [-1, 0, 0, 1]
    dz = ['L', 'D', 'U', 'R']
    cnt = 0
    queue = deque()
    
    queue.append({"red":red, "blue":blue, "cnt":0})
    while(queue):
        elem = queue.popleft()
        elem["cnt"] = elem["cnt"] + 1
        # print("in-----", elem)
        for idx in range(4):
            # 어느 구슬먼저 움직일지 결정
            order = setOrder(elem["red"], elem["blue"], dz[idx])

            first = elem[order[0]]
            second = elem[order[1]]
            move_cnt = 0    # red, blue 둘다 한번도 안움직였다면, 큐에 넣지않음. 넣을 필요없음.

            while(True):    # 기울여서 구슬 움직이기
                # print("------check ", first, second, idx)
                if board[first[0]+dx[idx]][first[1]+dy[idx]] == '#':
                    break
                elif board[first[0]+dx[idx]][first[1]+dy[idx]] == 'O':
                    first = [-1,-1]
                    break
                else:
                    first = [first[0]+dx[idx], first[1]+dy[idx]]
                    move_cnt = move_cnt + 1
                    # print("check ", board[first[0]][first[1]], first)
            
            while(True):
                # print("------check ", first, second, idx)
                if board[second[0]+dx[idx]][second[1]+dy[idx]] == '#' or first == [second[0]+dx[idx], second[1]+dy[idx]]: # 겹치는 경우 체크
                    break
                elif board[second[0]+dx[idx]][second[1]+dy[idx]] == 'O':
                    second = [-1,-1]
                    break
                else:
                    second = [second[0]+dx[idx], second[1]+dy[idx]]
                    move_cnt = move_cnt + 1

            # print("out---- ", first, second, dz[idx])

            # 구멍에 빠졌는지 확인
            if first == [-1,-1] and second == [-1,-1]: # 두개 모두 빠졌을 때
                continue
            elif (first == [-1,-1] and order[0] == 'blue') or (second == [-1,-1] and order[1] == 'blue'):
                continue
            elif (first == [-1,-1] and order[0] == 'red') or (second == [-1,-1] and order[1] == 'red'):
                # print("Success!!!")
                # print(order)
                # print(first, second, elem["cnt"])
                print(1)
                exit()
            else:


                if move_cnt != 0 and elem["cnt"] < 10:   # 10번 이하라면 큐에 삽입
                    new_elem = {order[0]:first, order[1]:second, "cnt":elem["cnt"]}
                    queue.append(new_elem)
                    # print(new_elem, dz[idx])
                    
    
    print(0)
    exit()