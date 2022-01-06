'''
    노드 클래스를 만들어서 구조화한 후 뎁스를 탑-다운 순서로 계산
'''

from collections import deque

class node:

    def __init__(self, num, depth):
        self.num = num
        self.child = []
        self.depth = depth

    def __repr__(self) -> str:
        return ("{} {} {}".format(self.num, self.child, self.depth))

    

if __name__ == '__main__':

    N = int(input())
    root = -1
    nodes = [node(None, None) for _ in range(21)] # max = 21

    for n in range(1, N+1):
        num = int(input())

        if num == -1:   # 루트노드 저장
            root = n
            nodes[n].num = -1
            nodes[n].depth = 0
        else:
            nodes[n].num = n          # 노드번호 저장
            nodes[num].child.append(n)  # 자식 추가


    # for n in range(1, N+1):
    #     print(nodes[n])    

    queue = deque()
    queue.append(root)
    while(queue):
        cur_idx = queue.popleft()
        for i in range(len(nodes[cur_idx].child)):
            child_idx = nodes[cur_idx].child[i] # 자식노드 찾기
            queue.append(child_idx)             # 큐에 추가

            nodes[child_idx].depth = nodes[cur_idx].depth+1 # 뎁스 계산
            
    for n in range(1, N+1):
        print(nodes[n].depth)


