'''
    Disjoint-Set으로 풀이
    
    Union-Find 연산을 이용해서 집합을 찾아 정답 계산
'''

import sys

class disjointSet :

    parent = {}
    rank = {}

    def __init__(self, ):
        self.parent, self.rank = {}, {}

    def find(self, v):
        try:
            if self.parent[v] != v :
                self.parent[v] = self.find(self.parent[v])
        except KeyError:
            self.parent[v] = v
            self.rank[v] = 0
        finally:
            return self.parent[v]

    def union(self, v1, v2):
        v1_root = self.find(v1)
        v2_root = self.find(v2)

        if v1_root != v2_root:

            v1_rank = self.rank[v1_root]
            v2_rank = self.rank[v2_root]

            if v1_rank < v2_rank:
                self.parent[v1_root] = v2_root
            else:
                self.parent[v2_root] = v1_root
            if v1_rank == v2_rank:
                self.rank[v2_root] += 1

if __name__ == "__main__":
    U = disjointSet()

    N, M = map(int, input().split())

    for _ in range(M):
        line = list(map(int, sys.stdin.readline().rstrip().split()))
        U.union(line[0], line[1])

        # print(U.parent)
        # print(U.rank)

    # print( list(U.rank.values()).count(0) )
    count = 0
    for i in range(1, N+1):
        try:
            if U.rank[i] == 0:
                count += 1
        except KeyError:
            count += 1

    print(count)
