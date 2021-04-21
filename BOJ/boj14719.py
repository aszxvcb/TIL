# 빗물

''' 물이 고일 수 있는 영역 탐색 '''            
def waterCheck(line):
    left = -1; right = -1
    cnt = 0
    for x in range(len(line)):
        if left == -1:
            if line[x] == 1:
                left = x
        else:
            if line[x] == 1:
                right = x

        if left != -1 and right != -1:
            cnt += right-1 - left
            left = right
            right = -1
    # print(cnt)
    return cnt

if __name__ == "__main__":
    answer = 0
    H, W = list(map(int, input().split()))
    blockList = list(map(int, input().split()))

    world = [[ 0 for _ in range(W) ] for _ in range(H) ]
    
    '''블록 준비 -> 세로획 하나씩 아래에서 위로 블록을 쌓음'''
    for x in range(W):
        for dy in range(blockList[x]):
            world[H-dy-1][x] = 1
    
    for line in world:
        print(line)

    '''바닥 행부터 탐색'''
    for dy in range(H):
        line = world[H-dy-1]
        # print(line)
        answer += waterCheck(line)

    print(answer)

