def solution(arr):
    answer = []
    
    for i in arr:
        if len(answer) == 0:
            answer.append(i)
        else:
            if(answer[-1] != i):
                answer.append(i)


    return answer


if __name__ == "__main__":
    arr = [1,1,3,3,0,1,1]
    ret = solution(arr)
    print(ret)