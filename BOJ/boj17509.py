from collections import deque

def solution(target):
    # print(target)

    # print(dic)
    leftCheck = False
    rightCheck = False

    for i in range(0, target):
        leftNum =  target - i
        rightNum = target + i
        
        if possibleCheck(leftNum) == True and leftNum <= 200:
            leftCheck = True
        
        if possibleCheck(rightNum) == True and rightNum <= 200:
            rightCheck = True

        if leftCheck == True or rightCheck == True:
            return leftNum if leftCheck == True else rightNum
            
    

def possibleCheck(num):
## 입력된 값이 바로 만들 수 있는 수인지 체크

    num = list(str(num))
    # print(num)
    for idx, elem in enumerate(num):
        # print(idx, elem)
        if idx+1 < len(num):
            if int(num[idx+1]) not in dic[int(num[idx])]: # 뒤에 숫자가 현재 숫자 기준, 나올 수 없는 수라면 False
                return False
    else:
        return True
         


if __name__ == "__main__":
    
    global dic
    dic = {}
    dic[0] = [0]
    dic[1] = [1,2,3,4,5,6,7,8,9,0]
    dic[2] = [2,3,5,6,8,9,0]
    dic[3] = [3,6,9]
    dic[4] = [4,5,6,7,8,9,0]
    dic[5] = [5,6,8,9,0]
    dic[6] = [6,9]
    dic[7] = [7,8,9,0]
    dic[8] = [8,9,0]
    dic[9] = [9]

    TC = int(input())
    for _ in range(TC):
        num = int(input())
        ret = solution(num)

        print(ret)
