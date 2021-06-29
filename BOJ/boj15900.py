'''
    1번부터 모든 노드를 순회하는데,
        노드의 방문수가 짝수이면 No
        노드의 방문수가 홀수이면 Yes

    모든 리프 노드들의 뎁스의 합을 구함

    시간초과 발생
    - visit의 여부를 array의 in으로 체크하면, O(n)만큼의 시간이 소요된다.
    visit의 여부를 딕셔너리 자료구조로 체크
    - pypy로 컴파일
'''

import sys

def solution(tree):
    visit = {}
    stack = [[1,0]]
    answer = 0
    while(stack):
        v = stack.pop()
        if visit.get(v[0], None) != None:
            continue
        
        visit[v[0]] = True
        
        # 리프 노드인 경우
        if len(tree[v[0]]) == 1 and v[0] != 1:
            # print(v)
            answer += v[1]
        # 내부 노드인 경우
        else: 
            for conn_v in tree[v[0]]:
                if visit.get(conn_v, None) != None:
                    continue
            
                stack.append([conn_v, v[1]+1])

    # print(answer)
    if answer % 2 == 0:
        print("No")
    else:
        print("Yes")

if __name__ == "__main__":
    N = int(input())
    
    tree = {}
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        if tree.get(a, None) == None:
            tree[a] = [b]
        else:
            tree[a].append(b)

        if tree.get(b, None) == None:
            tree[b] = [a]
        else:
            tree[b].append(a)

    solution(tree)