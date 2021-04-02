from collections import deque

def solution(progresses, speeds):
    answer = []

    deq_progresses = deque(progresses)
    deq_speeds = deque(speeds)

    while(len(deq_progresses) != 0):
        for i in range(0, len(deq_progresses)):
            deq_progresses[i] += deq_speeds[i]

        cnt = 0
        while( len(deq_progresses) != 0 and deq_progresses[0] >= 100 ):
            cnt += 1
            deq_progresses.popleft()
            deq_speeds.popleft()
        if( cnt != 0 ):
            answer.append(cnt)
        
    return answer

if __name__ == "__main__":
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]

    ret = solution(progresses, speeds)
    print(ret)