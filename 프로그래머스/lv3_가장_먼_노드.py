from collections import deque

global graph
global distance
global queue
global visit
global con_list

'''
    인접행렬, BFS 를 이용한 문제 풀이 => 크기가 커지면 시간초과 발생
    초기 준비에서 시간이 오래 걸리는 것 같아서 ( 특히 list comprehension 이라고 생각했었음 )
    크기 선언을 '[0] * n' 과 같이 수정하였다.

    하지만 얕은복사 문제로 인해 2차원 배열에서 문제가 발생.
    참고 : https://yechoi.tistory.com/52

    인접행렬 -> 인접리스트로 문제 접근
'''

def BFS(start):
    global visit, queue, graph, distance, con_list

    queue.append([start,0])
    visit[start] = True
    distance[0] = 0
    '''
    while(queue):
        # print(queue)
        start, cnt = queue.popleft()
        # print(start+1)
        for node in range(len(visit)):
            if( graph[start][node] == 1 and visit[node] == False ):
                queue.append([node,cnt+1])
                visit[node] = True
                if( distance[node] > cnt+1 ):
                    distance[node] = cnt+1
    '''
    while(queue):
        # print(queue)
        start, cnt = queue.popleft()
        # print(start+1)
        for node in (con_list[start]):
            if( visit[node] == False ):
                queue.append([node,cnt+1])
                visit[node] = True
                if( distance[node] > cnt+1 ):
                    distance[node] = cnt+1                    

def solution(n, edge):
    answer = 0
    # global graph
    # graph = [[ 0 for _ in range(0,n) ] for _ in range(0, n)]
    # graph = [[0] * n  for _ in range(n)]

    global con_list
    con_list = { node:[] for node in range(n)}

    global distance
    # distance = [ float('inf') for _ in range(n) ]
    distance = [ float('inf') ] * n
    global queue
    queue = deque()
    global visit
    visit = [ False ] * n

    for line in edge:
        x, y = line
        # graph[x-1][y-1] = 1
        # graph[y-1][x-1] = 1
        con_list[x-1].append(y-1)
        con_list[y-1].append(x-1)
        # print(x, y, graph)
    # print(con_list)
    # for line in graph:
        # print(line)

    BFS(0)
    
    # print(distance)
    answer = distance.count(max(distance))
    return answer

if __name__ == "__main__":
    ret = solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
    print(ret)