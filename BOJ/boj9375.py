'''
    옷의 종류를 key로 하는 딕셔너리(해시테이블)을 만든 후,
    가능한 조합의 개수를 구함
    value의 갯수가 1이 아닌 경우는, 그 만큼 곱셈하여 계산
'''
from itertools import combinations

def solution(dic):
    answer = 0
    possible_comb = []
    keys = list(dic.keys())

    for key in keys:
        answer += len(dic[key])

    if len(keys) >= 2:
        for i in range(2,len(keys)+1):
            combs = list(combinations(keys,i))
            for comb in combs:
                num = 1
                for key in comb:
                    num *= len(dic[key])
                answer += num
                
    print(answer)


'''
## 메모리 초과
def solution(dic):
    answer = 0
    possible_comb = []
    keys = list(dic.keys())

    for key in keys:
        possible_comb.append([key])

    if len(keys) >= 2:
        for i in range(2,len(keys)+1):
            possible_comb.extend(list(combinations(keys,i)))

    # print(possible_comb)
    
    for target in possible_comb:
        num = 1
        for i in range(len(target)):
            num *= len(dic[target[i]])
        else:
            answer += num

    print(answer)
'''

if __name__ == "__main__":
    TC = int(input())
    
    for _ in range(TC):
        dic = {}
        n = int(input())
        for _ in range(n):
            name, kind = input().split()
            if dic.get(kind, None) == None:
                dic[kind] = [name]
            else:
                dic[kind].append(name)

        solution(dic)
        
