from collections import deque

'''
    location을 어떻게 관리할까 고민하다가, 계속 변경해주는 방식으로 해결했는데,
    enumerate를 사용해서 인덱스를 미리 저장해놓고 사용하면, 그럴 필요가 없어짐.
'''

def solution( prioirities, location):
    answer = 0
    cnt = 0
    deq = deque(prioirities)

    while( location != -1 ):
        if( deq[0] != max(deq)):
            deq.append(deq.popleft())
            if location == 0:
                location = len(deq)-1
            else:
                location -= 1
        else:
            deq.popleft()
            cnt += 1
            location -= 1

        # print(deq, location)

    answer = cnt

    return answer

# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     answer = 0
#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer


if __name__ == "__main__":
    ret = solution([2, 1, 3, 2], 2)
    print(ret)

    ret = solution([1, 1, 9, 1, 1, 1], 0)
    print(ret)