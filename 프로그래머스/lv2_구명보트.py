from collections import deque

'''
    처음에는 list를 이용한 풀이를 진행,
    정렬 후, 처음 원소와 마지막 원소를 비교하여 
    limit 을 넘어가면 마지막 원소만을 태운 보트 사용,
    limit 을 넘지않는다면 처음과 마지막 원소를 태운 보트를 사용

    시간초과 발생 => 리스트 pop(0)을 하게되면, 뒤에 원소를 한칸씩 앞으로 쉬프트하는데에 시간이 오래 걸림
    첫번째 해결 방법으로는 라인 슬라이싱 사용. 하지만 해결되지 않음
    
    두번째 방법으로 deque 자료구조 사용. => 해결

'''

def solution(people, limit):
    answer = 0
    
    people.sort()
    queue = deque(people)
    
    while( len(queue) != 0 ):
        if len(queue) > 1 and queue[0] + queue[-1] <= limit:
            queue.pop()
            queue.popleft()
            answer += 1
        else :
            queue.pop()
            answer += 1
    
    return answer

if __name__ == "__main__":
    people = [70, 80, 50]
    limit = 100
    ret = solution(people, limit)
    print(ret)