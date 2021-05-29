'''
    투포인터를 이용하여 연속된 노드 중 가장 많은 종류를 먹을 수 있는 경우를 탐색
    
    카운트를 효율적으로 하기위해 딕셔너리를 만들어, 나온 수를 체크하여 중복체크와 동시에 셈을 해준다.
'''

import sys, copy
from collections import deque

def solution(d,k,c,nodes):
    answer = 1
    lp, rp = 0, 0
    window = deque()
    dic_window = {(node+1):0 for node in range(d)}
    dic_window[c] += 1   # 쿠폰은 미리 추가
    max_answer = 1
    
    # 초기 k개의 노드
    for i in range(k):
        rp += 1
        window.append(nodes[i])
        dic_window[nodes[i]] += 1
        
        if dic_window[nodes[i]] == 1:
            answer += 1

    # 왼쪽 포인터가 마지막까지 도달하면 종료
    while( lp != len(nodes)-1 ):

        # 왼쪽 포인터 이동
        elem = window.popleft()
        dic_window[elem] -= 1
        lp += 1
        if dic_window[elem] == 0:
            answer -= 1

        # 오른쪽 포인터 이동
        window.append(nodes[rp])
        dic_window[nodes[rp]] += 1
        if dic_window[nodes[rp]] == 1:
            answer += 1

        rp += 1
        # 오른쪽 노드는 넘어가면 왼쪽끝으로 이동
        if rp == len(nodes) :
             rp = 0

        if answer > max_answer:
            max_answer = answer


    # print(window)
    print(max_answer)

    return


if __name__ == "__main__":
    N, d, k, c = map(int, input().split())
    nodes = []
    for _ in range(N):
        nodes.append(int(sys.stdin.readline().rstrip()))
    solution(d, k, c, nodes)