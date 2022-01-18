import heapq, sys

if __name__ == "__main__":
    TC = int(input())
    pq = []

    for _ in range(TC):
        i = int(sys.stdin.readline().rstrip())
        if i == 0:
            try:
                print(heapq.heappop(pq))
            except IndexError:
                print("0")
        else:
            heapq.heappush(pq, i)
