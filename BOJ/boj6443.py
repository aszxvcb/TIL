'''
 메모리초과, 시간초과
 순열을 구할 때, 이미 구한 순열을 또 구하거나
 정렬을 수행하면서 리소스를 모두 사용하는 것 같음

 중복되지 않도록 순열을 구하는 것이 필요함.

 중복이 없는 순열의 경우의수.
 5!/3!2! -> 5자리 수의 순열 중, 3개와 2개가 겹치는 경우


 solution3() -> 맞았습니다.
 itertool.permutations 사용시, 메모리초과와 시간초과 발생
 동일한 순열을 만들어내면서, 메모리와 시간을 잡아먹기 때문.
 순열을 생성하는 과정에서 동일한 값을 사전에 제외하는 백트래킹 과정이 필요
'''

from itertools import permutations
import math
from functools import reduce

def DFS(prefix, visit):
    if 0 not in visit:
        print(prefix)
        return
    
    for idx, elem in enumerate(ss):
        if visit[idx] == 0:
            if prefix + ss[idx] not in perm_set:
                visit[idx] = 1
                perm_set.add(prefix)
                DFS(prefix + ss[idx], visit)
                visit[idx] = 0


def solution3(s):
    global ss, perm_set
    visit = [0] * len(s)
    ss = s
    perm_set = set()

    DFS('', visit)


def solution2(s):
    
    permu_set = set()
    list(map(lambda x: permu_set.add(''.join(x)), list(permutations(s))))

    for elem in sorted(list(permu_set)):
        print(elem)

def solution(s):

    perm = permutations(s)
    dic = {}
    cnt = 0
    max_cnt = 0

    ## 입력된 문자 중복갯수 체크
    dic = { 'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0 }
    for char in s:
        dic[char] = dic[char] + 1

    max_cnt = (int(math.factorial(len(s)) / reduce( lambda acc, cur: acc * math.factorial(dic[cur]) , dic.keys(), 1)))

    while(cnt < max_cnt):
        try:
            elem = ''.join(list(next(perm)))
            
            if dic[elem] == 1:
                continue
        except KeyError:
            dic[elem] = 1
            print(elem)
            cnt = cnt + 1
        except:
            break
    
if __name__ == '__main__':

    TC = int(input())

    for _ in range(TC):
        s = list(input())
        s.sort()
        solution3(s)

