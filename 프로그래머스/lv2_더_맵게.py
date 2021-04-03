import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    # print(scoville)
    cnt = 0

    while ( scoville[0] < K and len(scoville) >= 2):
        first_scv = heapq.heappop(scoville)
        second_scv = heapq.heappop(scoville)

        if( first_scv == 0 and second_scv == 0):
            return -1

        new_scv = first_scv + (second_scv * 2)
        heapq.heappush(scoville, new_scv)
        cnt += 1

    if( scoville[0] < K ):
        return -1

    answer = cnt
    return answer

if __name__ == "__main__":
    ret = solution([1,2,0], 7)
    print(ret)