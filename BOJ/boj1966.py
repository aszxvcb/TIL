from collections import deque

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        queue = deque(list(map(list, zip(input().split(), [0]*N))))
        queue[M][1] = 1
        cnt = 1
        # print(queue)
        while(True):
            q = queue.popleft()
            if len(queue) > 0 and max(queue, key=lambda x:x[0])[0] > q[0]:
                queue.append(q)
            else:
                # print(q)
                if q[1] == 1:
                    print(cnt)
                    break
                else:
                    cnt += 1
