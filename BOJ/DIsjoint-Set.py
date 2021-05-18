'''
    Disjoint-Set : https://onepwnman.github.io/Disjoint-Set-Data-Structure/
'''

class UnionFind(object):

    parent = {}
    rank = {}

    def __init__(self, ):
        self.parent, self.rank = {}, {}

    def __repr__(self, ):
        sets = {}
        for key in self.parent:
            parent = self[key]
            if parent not in sets:
                sets[parent] = [key]
            else:
                sets[parent].append(key)
        return 'Disjoint-set : ' + str(sets)

    def get_parent(self, ):
        return self.parent

    def __getitem__(self, x):
        return self.find(x)

    def find(self, x):

        try:
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
        except KeyError:
            self.parent[x], self.rank[x] = x,0
        finally:
            return self.parent[x]


    def union(self, x, y):
        x, y = self[x], self[y]
        if x != y:  # 두 정점의 루트가 같지 않다면
            if self.rank[x] < self.rank[y] :    # 뎁스가 큰 트리 밑에 작은 트리를 연결
                self.parent[x] = y
            else:
                self.parent[y] = x
            if self.rank[x] == self.rank[y]:    # 랭크가 같다면, 한쪽에 연결하고 rank+1
                self.rank[y] += 1
                    


if __name__ == "__main__":

    u = UnionFind()

    # u.union(u['1'], u['2'])
    # u.union(u['2'], u['5'])
    # u.union(u['5'], u['1'])
    # u.union(u['3'], u['4'])
    # u.union(u['4'], u['6'])
    # print(u.parent)
    # print(u.rank)
    # u.union(u['5'], u['4'])
    # print(u.parent)
    # print(u.rank)
    # u.union(u['2'], u['4'])
    # print(u.parent)
    # print(u.rank)
    # u.union(u['2'], u['3'])
    # print(u.parent)
    # print(u.rank)

    u.union(u['0'],u['1'])
    print(u)
    print(u.rank)
    u.union(u['3'],u['4'])
    print(u)
    print(u.rank)
    u.union(u['5'],u['6'])
    print(u)
    print(u.rank)
    u.union(u['1'],u['2'])
    print(u)
    print(u.rank)
    u.union(u['3'],u['6'])
    print(u)
    print(u.rank)
    u.union(u['0'],u['6'])
    print(u)
    print(u.rank)