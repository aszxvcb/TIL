import heapq, sys

PQ = []

N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        if len(PQ) == 0:
            print(0)
        else:
            print(heapq.heappop(PQ))
    else:
        heapq.heappush(PQ, num)