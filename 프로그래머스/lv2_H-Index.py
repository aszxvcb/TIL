'''
    citations 을 정렬 후,
    각 인덱스에서 가능한 숫자의 범위를 탐색 후, 리스트에 저장한다.
    이후 리스트에서 최대값을 찾아 리턴

    //todo 큰 값부터 찾는다면, 시간복잡도를 줄일 수 있을 것 같은데
'''

def solution(citations):
    answer = 0
    citations.sort()
    candidate = []
    # print(citations)
    
    for num in reversed(range(1, len(citations)+1)):
        for i in range(0, citations[len(citations)-num]+1):
            if ( i <= num ):
                candidate.append(i)
            print(candidate)

    answer = max(candidate)
    return answer

if __name__ == "__main__":
    ret = solution([0,0,0,3])
    print(ret)