'''
    현 주유소보다 싼 주유소까지 남은 거리만큼 기름을 넣어야함

    => 현 주유소보다 싼 주유소를 만나면, 지금까지 지나온 거리만큼 기름값을 계산
'''

def solution(distances, cities):
    answer = 0
    cur = cities[0]
    distance = 0
    cnt = 0

    cities = cities[1:]

    for idx in range(len(cities)):
        distance += distances[idx]
        if cur > cities[idx]:
            answer += cur * distance
            distance = 0
            cur = cities[idx]
    
    if distance != 0:
        answer += cur * distance

    return answer
        

if __name__ == "__main__":
    N = int(input())
    distances = list(map(int,input().split()))
    cities = list(map(int, input().split()))

    ret = solution(distances, cities)
    print(ret)