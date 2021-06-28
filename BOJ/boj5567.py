'''
    BFS로 탐색하고, 뎁스를 고려해서 정답을 구해낸다.
'''

import sys
from queue import deque

def solution(friends):
    answer = []
    if friends.get(1, None) == None:
        print(0)
        return
    
    queue =  deque([ [i, 1] for i in friends[1] ])
    
    while( queue ):
        q = queue.popleft()
        sid = q[0]
        depth = q[1]

        if depth <= 2 and sid not in answer and sid != 1:
            answer.append(sid)
        else:
            continue

        for elem in friends[sid]:
            # print(elem)
            if elem in answer:
                continue

            queue.append([elem,depth+1])

    print(len(answer))

if __name__ == "__main__":
    n = int(input())
    m = int(input())

    friends = {}
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        if friends.get(a, None) == None :
            friends[a] = [b]
        else:
            friends[a].append(b)

        if friends.get(b, None) == None :
            friends[b] = [a]
        else:
            friends[b].append(a)

    # print(friends)
    solution(friends)
