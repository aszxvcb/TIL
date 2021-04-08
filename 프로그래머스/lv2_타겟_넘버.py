answer = 0
def DFS(numbers, target, idx, num):
    global answer
    
    if num == target:
        answer += 1
        return answer

    if idx+1 != len(numbers):   
        DFS(numbers, target, idx+1, num + numbers[idx+1])
        DFS(numbers, target, idx+1, num - numbers[idx+1])

def solution(numbers, target):
    global answer
    
    DFS(numbers, target, 0, 0)
    
    return answer
    
if __name__ == "__main__":
    ret = solution([1, 1, 1, 1, 1], 3)
    print(ret)