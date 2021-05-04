'''
    현재 상태에서 더했을 때 만들 수 있는 가장 작은 값들을 찾아감

    최소힙을 이용하여 작은값들을 찾아냄
'''
import sys
import heapq

def solution(arr):
    answer = 0
    heapq.heapify(arr)

    answer = heapq.heappop(arr) + heapq.heappop(arr)
    heapq.heappush(arr, answer)
    # print(arr)
    # print(answer)
    while len(arr) > 1:
        # print(arr)
        temp = heapq.heappop(arr) + heapq.heappop(arr)
        # print(temp, answer)
        answer += temp
        heapq.heappush(arr, temp)
    
    # print(answer)
    return answer

if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        N = int(sys.stdin.readline().rstrip())
        arr = list(map(int, sys.stdin.readline().split()))

        ret = solution(arr)
        print(ret)