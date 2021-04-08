def DFS(i, computers):
    if visit[i] is False:
        visit[i] = True
    else:
        return
    
    for j in range(0, len(computers[i])):
        if computers[i][j] == 1:
            DFS(j, computers)

def solution(n, computers):
    global answer
    answer = 0
    global visit
    visit = [ False for i in range(0,len(computers)) ]
    
    for i in range(0, len(computers)):
        if( visit [i] is False ):
            DFS(i, computers)
            answer += 1
    
    return answer

if __name__ == "__main__":
    ret = solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    print(ret)