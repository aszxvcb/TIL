'''
    걸린시간 : 시간초과
    중간값을 출력하는 문제
    처음에는 하나의 힙을 이용하여 현재 힙의 들어온 갯수로 중간번째를 계산하고
    heappop()을 반복하여 중간값을 출력했다.
    하지만 시간초과 발생

    다른 사람들의 답안을 확인해보니
    최대힙, 최소힙 하나씩 두개의 힙큐를 사용하면 중간값을 한번에 구할 수 있다.
    최대힙의 top 값이 중간값이 되도록
    입력되는 숫자를 두개의 힙에 나누어 담는다.

    참고 : https://yabmoons.tistory.com/478
'''
import heapq, sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    maxHeap = []    # 중앙값과 중앙값보다 작은 수들이 삽입
    minHeap = []    # 중앙값보다 큰 값들을 삽입

    for _ in range(N):
        num = int(sys.stdin.readline())
        
        # 최대힙은 항상 최소힙과 같거나 +1의 크기를 가진다
        if len(maxHeap) == len(minHeap):
            heapq.heappush(maxHeap, -num)
        
        elif len(maxHeap)-1 == len(minHeap):
            heapq.heappush(minHeap, num)

        # 최대힙의 탑이 최소힙의 탑보다 크다면
        # 두 힙의 top을 스왑
        if (len(maxHeap) > 0 and len(minHeap) > 0) \
            and -maxHeap[0] > minHeap[0]:
            min_temp = heapq.heappop(minHeap)
            max_temp = -(heapq.heappop(maxHeap))
            heapq.heappush(minHeap, max_temp)
            heapq.heappush(maxHeap, -min_temp)
        
        print(maxHeap) # 최대힙을 위해서 -를 곱해줌
        print(minHeap)
        print(-maxHeap[0])