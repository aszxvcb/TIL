# 올림픽
'''
    입력받은 메달을 금>은>동 순의 우선순위를 부여해서 정렬

    순위를 계산할때는 정렬된 순서에서에서 차례로 확인
    이때 previous값은 갱신하면서 동일한 메달 수를 확인한다
    동일한 메달 수가 존재할 경우 same_cnt+=1 하고, rank는 변하지 않는다

'''
def solution(scoreboard, K):
    scoreboard.sort( key=lambda x:x[1]  ,reverse = True )
    # print(scoreboard)

    rank = 0
    same_cnt = 0
    previous = [-1,-1,-1]
    '''
    [(1, [3, 0, 0]), (4, [0, 2, 0]), (2, [0, 2, 0]), (3, [0, 0, 2])]
    나라번호와 메달수를 튜플로 가짐
    '''
    for score in scoreboard:
        if score[1] != previous:    # 메달 수의 중복 확인
            rank += 1 + same_cnt
            same_cnt = 0
        else:
            same_cnt += 1
        
        previous = score[1]         # 현재 메달 수를 저장
        
        if score[0] == K:           # 현재 탐색 중인 나라번호와 찾고자했던 번호가 같다면 리턴
            return rank


if __name__ == "__main__":
    N, K = map(int, input().split())
    scoreboard = []
    for _ in range(N):
        line = list(map(int, input().split()))
        scoreboard.append((line[0], line[1:]))
    # print(scoreboard)
    
    ret = solution(scoreboard, K)
    print(ret)