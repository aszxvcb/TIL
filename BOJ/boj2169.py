'''
    dp 기본예제 (아래, 오른쪽만 가능) 에서 조건이 추가된 문제 (왼쪽)
    오른쪽의 최적을 찾고, 왼쪽의 최적을 찾은 후, 두개사이의 최적을 다시 계산하면 된다.

    문제풀이 후 다른 코드를 보니, dp를 3차원 배열로 만들어서 계산한 경우도 있음.
'''

import copy

def solution(N,M,MAP):
    dp_right = [[0]*M for i in range(N)]
    dp_left = [[0]*M for i in range(N)]
    dp_opt =  [[0]*M for i in range(N)]
    
    dp_right[0] = copy.deepcopy(MAP[0])
    dp_left[0] = copy.deepcopy(MAP[0])
    
    # 첫번째 행의 최적값 계산
    optimize_num = 0
    for i in range(M):
        optimize_num += MAP[0][i]
        dp_opt[0][i] = optimize_num
    
    for n in range(1,N):
        #아래, 오른쪽만 가는 최적 경로
        for m in range(M):
            if m == 0 :
                dp_right[n][m] = dp_opt[n-1][m]+MAP[n][m]
            else:
                dp_right[n][m] = max([dp_right[n][m-1]+MAP[n][m], dp_opt[n-1][m]+MAP[n][m]])
        
        #아래, 왼쪽만 가는 최적 경로
        for m in reversed(range(M)):
            if m==M-1:
                dp_left[n][m] = dp_opt[n-1][m]+MAP[n][m]
            else:
                dp_left[n][m] = max([dp_opt[n-1][m]+MAP[n][m], dp_left[n][m+1]+MAP[n][m]])

        # 두 최적값 중 더 좋은 방법
        for m in range(M):
            dp_opt[n][m] = max([dp_left[n][m], dp_right[n][m]])
        
    # print(dp_right)
    print('='*10)
    for line in dp_right:
        print(line)
    print('='*10)
    # print(dp_left)
    for line in dp_left:
        print(line)
    print('='*10)
    # print(dp_opt)
    for line in dp_opt:
        print(line)

    return dp_opt

if __name__ == "__main__":
    N = 5; M = 5
    MAP = [[10,25,7,8,13],[68,24,-78,63,32], [12,-69,100,-29,-25],[-16,-22,-57,-33,99],[7,-76,-11,77,15]]

    # N,M = map(int, input().split())  
    # MAP = []
    # for _ in range(N):
    #     MAP.append( list(map(int, input().split())) )
    # print(MAP)
    
    ret = solution(N,M,MAP)
    print(ret[N-1][M-1])