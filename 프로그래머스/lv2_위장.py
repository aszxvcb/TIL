from functools import reduce
from collections import Counter
from itertools import combinations

'''
    조합의 갯수만 찾으면 되기 때문에, 경우의 수 공식 이용    
'''
def solution(clothes):
    answer = 0

    cnt = Counter([kind for name, kind in clothes])

    answer = reduce(lambda x,y : x*(y+1), cnt.values(), 1) - 1

    return answer 


'''
# 가능한 모든 조합을 구해서 갯수를 세는 것은 시간초과 발생
def solution(clothes):
    answer = 0

    dic = {}
    for x,y in clothes:
        dic[x] = y

    answer += len(clothes)
    for i in range(2,len(dic.keys())+1):
        for c in combinations(dic.values(),i):
            check = {}
            for elem in c:
                if (elem not in check):
                    check[elem] = 1
                else:
                    break
            else:
                print(c)
                answer += 1

    return answer
'''

if __name__ == "__main__":
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    ret = solution(clothes)

    print( ret )