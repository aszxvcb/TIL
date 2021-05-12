'''
    각 자리수가 커지기 위해서는
    높은 자리수 일수록 큰 수를 가져가야함
    같은 자리의 두개의 문자를 고려할 떄는
    뒤에 나온 수가 많은거에 우선 순위를 줄 수 있음 (x)
    
    뒤에 나온 수가 먼저 나온 문자에 우선 순위

    // 그리디 참고 : https://imnotabear.tistory.com/85
'''
import heapq

def solution(str_arr):
    answer = 0
    numbers = [0,1,2,3,4,5,6,7,8,9]

    # 모든 숫자를 이어붙힌 str3 정의
    str3 = ""
    for s in str_arr:
        str3 += s
    # print(str3)

    atoi_dic = {}
    arr = []

    # [자릿수, 총 나온 수, 들어온 순서,'문자'] 를 우선순위큐에 넣음
    for s in str_arr:
        for i in range(len(s)):
            char = s[i]
            temp = [-(len(s)-i), -(list(str3).count(char)), s.index(char), char]
            arr.append(temp)
    # print(arr)
    heapq.heapify(arr)
    
    # 우선순위큐에서 주어진 우선순위대로 하나씩 빼서, 숫자 부여
    while arr:
        elem = heapq.heappop(arr)
        # print(elem)
        if atoi_dic.get(elem[3], None) == None:
            atoi_dic[elem[3]] = numbers.pop()

    # print(atoi_dic)

    # 부여된 숫자로 재계산
    for s in str_arr:
        new_str = ""
        for i in range(len(s)):
            new_str += str(atoi_dic[s[i]])

        # print(new_str)
        answer += int(new_str)

    print(answer)


if __name__ == "__main__":
    N = int(input())
    str_arr = []
    for i in range(N):
        str_arr.append(input())

    solution(str_arr)
