def solution(arr):
    # print(arr)
    dic = {}

    # 딕셔너리를 이용자여 저장
    for elem in arr:
        try:
            dic[elem] = dic[elem] + 1
        except: 
            dic[elem] = 1

    # 배열에 넣어 정렬
    ret_arr = []
    for elem in dic:
        ret_arr.append([elem, dic[elem]])
    ret_arr.sort()

    # 출력
    for elem in ret_arr:
        print("{} {}".format(elem[0] , elem[1] ))

if __name__ == "__main__":
    TC = int(input())
    
    arr = []
    for _ in range(TC):
        arr.append(input().split('.')[-1])

    solution(arr)
        