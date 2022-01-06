'''
    [S+dx, T+dy, depth]
    queue 를 이용한 문제풀이
    너비우선탐색
'''
from collections import deque

def solution(S, T):
    q = deque()
    q.append([S,T,0])

    while( q ):
        s, t, d = q.popleft()
        # print(s,t,d)
        d = d+1

        if( s*2 == t+3 or s+1 == t ): # 가장 먼저 조건을 일치하면 그것이 정답
            # print(d)
            return d
        
        if( s*2 < t+3 ):              # 좌변이 우변보다 커지면, 큐에 넣을 필요가 없음
            q.append([s*2,t+3,d])
        if( s+1 < t ):
            q.append([s+1,t,d])


if __name__ == '__main__':
    N = int(input())
    
    for _ in range(N):
        S, T = map(int, input().split())
        print(solution(S, T))