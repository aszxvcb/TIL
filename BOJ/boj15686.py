'''
    걸린시간 : 40분
    
    구현 문제
    
    주어진 입력에서 집과 치킨집을 찾고, 순서대로 인덱스를 부여
    distance[][] 을 생성하여 한 집에서 갈 수 있는 치킨집의 거리를 모두 구함
    조합을 이용하여 가능한 치킨집의 조합들을 생성
    모든 조합 중 가장 짧은 거리를 가지는 값을 리턴
'''

from itertools import combinations

def solution(arr, M):
    # 집과 치킨집 찾기
    houses = []
    stores = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 1:
                houses.append((i+1,j+1))
            elif arr[i][j] == 2:
                stores.append((i+1,j+1))
    # print(houses)
    # print(stores)

    # 모든 값 구하기
    # distnace[i][j] = k ==> i번째 집에서 j번째 치킨집 사이의 거리
    distance = [ [float('INF')] * len(stores) for _ in range(len(houses)) ]
    
    for i in range(len(houses)):
        for j in range(len(stores)):
            house = houses[i]
            store = stores[j]

            dist = abs(house[0]-store[0]) + abs(house[1]-store[1])
            distance[i][j] = dist

    # for line in distance:
    #     print(line)

    # 최대 M개가 되는 조합 찾기
    # print("==== 조합 찾기 ====")
    possible = []
    idx_store = [ idx for idx, val in enumerate(stores)]

    for i in range(M):
        if i==0:
            [possible.append([idx]) for idx in idx_store]
        else:
            possible.extend(map(list, (combinations(idx_store, i+1))))
    # print(possible)

    # 모든 거리 계산
    result = []
    for pos in possible:
        num = 0
        for house in range(len(houses)):
            num += min([distance[house][idx] for idx in pos])
        result.append(num)
    
    # print(result)
    return min(result)

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    ret = solution(arr, M)
    print(ret)