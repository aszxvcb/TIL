'''
    MST, 크루스칼(간선을 이용한), Disjoint-Set
    union/find 함수가 중요

    https://onepwnman.github.io/MST/

    프림 알고리즘으로도 풀이가능
    -> 정점을 늘려가며 이웃하는 간선 중 가장 작은 순서대로
'''

import sys, heapq

rank = {}
parent = {}

def find(x):
    global parent

    try:
        if parent[x] != x:
            parent[x] = find(parent[x])
    except KeyError:
        parent[x] = x
        rank[x] = 0
    finally:
        return parent[x]

def union(x, y):
    x_root, y_root = find(x), find(y)

    if x_root != y_root:
        x_rank = rank[x_root]
        y_rank = rank[y_root]

        if x_rank < y_rank:
            parent[x_root] = y_root
        else:
            parent[y_root] = x_root
        if x_rank == y_rank:
            rank[y_root] += 1

        return True
    
    return False

def solution(vertex, edge):
    weight = 0
    num_con_ver = 1

    heapq.heapify(edge)

    while num_con_ver < len(vertex)-1:
        e = heapq.heappop(edge)
        # print(e)

        # cycle 체크
        if union(e[1], e[2]):
            # edge 추가
            weight += e[0]
            num_con_ver += 1

    # print
    global parent 
    sets = {}
    for key in parent:
        p = find(key)
        if p not in sets:
            sets[p] = [key]
        else:
            sets[p].append(key)
    # print( sets )

    print(weight)

 
if __name__ == "__main__":
    V, E = map(int, input().split())

    vertex = [0] * (V+1)    
    edge = []

    for _ in range(E):
        line = list(map(int, sys.stdin.readline().rstrip().split()))
        line[0], line[1], line[2] = line[2], line[0], line[1]

        if line[1] > line[2]:
            line[2], line[1] = line[1], line[2]

        edge.append(line)

    solution(vertex, edge)
