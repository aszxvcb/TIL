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
    # print(x_root, y_root)
    if x_root != y_root:
        x_rank = rank[x_root]
        y_rank = rank[y_root]

        # print( x_rank, y_rank )

        if x_rank < y_rank:
            parent[x_root] = y_root
        else:
            parent[y_root] = x_root
        if x_rank == y_rank:
            rank[y_root] += 1

        # print(parent)

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
    V = int(input())
    E = int(input())

    vertex = [0] * (V+1)    
    edge = []

    for _ in range(E):
        line = list(map(int, sys.stdin.readline().rstrip().split()))
        line[0], line[1], line[2] = line[2], line[0], line[1]

        if line[1] > line[2]:
            line[2], line[1] = line[1], line[2]

        edge.append(line)

    solution(vertex, edge)
