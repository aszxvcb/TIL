'''
    가능한 조합을 구한 후, 조건에 맞는지 확인
'''

from itertools import combinations

def solution(charset):
    answer = []

    global L, C
    combi = list(combinations(charset, L))
    must_have = ['a','e','i','o','u']
    
    for c in combi:
        # 자음 모음 갯수 확인
        consonant_cnt = 0
        vowel_cnt = 0

        cur = ''.join(c)
        
        # 하나 이상의 모음이 포함되었는지 체크
        for i in c:
            if i in must_have:
                vowel_cnt += 1
            else:
                consonant_cnt += 1

        if vowel_cnt < 1 or consonant_cnt < 2:
            continue

        # 정렬되어 있는지 확인
        sorted_cur = ''.join(sorted(c))
        if cur != sorted_cur:
            continue
        
        answer.append(cur)

    return answer     

if __name__ == "__main__":
    L, C = map(int, input().split())
    charset = input().split()
    charset = sorted(charset)
    # print(charset)

    ret = solution(charset)
    ret.sort()
    for elem in ret:
        print(elem)