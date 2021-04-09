global visit
global answer

'''
    가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 선택해야하므로
    sort()를 하여 사전순으로 정렬
    
    -> 실패 : 모든 항공권을 사용하지 못하는 케이스가 발생
    입력 : [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]
    결과 : ["ICN", "COO", "ICN", "BOO", "DOO"]
    
    알파벳 순서 + 모든 항공권 사용 조건을 만족해야함
    만약 모든 항공권을 사용하지 않았다면, DFS를 반복하는 것이 필요
'''

def DFS(tickets, start):
    if( False in visit ):
        for idx in range(0, len(tickets)):
            if((tickets[idx][0] == start) and (visit[idx] == False)):
                answer.append(tickets[idx][1])
                visit[idx] = True
                # print(answer, visit)
                DFS(tickets, tickets[idx][1])
                
                # 중요!
                if( False in visit ):
                    answer.pop()
                    visit[idx] = False
                    continue
                return

def solution(tickets):
    global visit
    visit = [ False for _ in range(0, len(tickets))]
    global answer
    answer = []
    
    answer.append("ICN")
    tickets.sort()
    # print(tickets)
    DFS(tickets, "ICN")
    
    return answer

if __name__ == "__main__":
    tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    ret = solution(tickets)
    print(ret)