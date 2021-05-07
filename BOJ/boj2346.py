'''
    걸린시간 : 1시간 이상
    
    리스트 -> 링크드리스트 -> 덱
    의 순으로 생각하며 풀이를 진행한 문제
    
    리스트로도 간단하게 구현할 수 있을 것 같아서 진행했다가 
    생각보다 고려해야할 경우가 많아 시간만 잡아먹음
    덱의 rotate를 이용하여 풀이
'''


from collections import deque

def solution(balloons):
    answer = []
    indexArr = deque([i+1 for i in range(len(balloons))])
    
    while( len(indexArr) != 0 ):
        idx = indexArr.popleft()
        num = balloons[idx-1]
        answer.append(idx)
        
        if num > 0:
            num -= 1
        else :
            num += 0
        
        indexArr.rotate(-num)
        # print(indexArr)

    return answer

if __name__ == "__main__":
    N = int(input())
    balloons = list(map(int, input().split()))

    ret = solution(balloons)
    print(" ".join(list(map(str, ret))))

