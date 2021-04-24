'''
    딕셔너리(맵)을 이용해서 각 문자의 갯수를 구하고, 나머지를 찾음
    
    팁 : chain(dic.items()) 으로 두개의 딕셔너리를 연결
'''

from itertools import chain

def solution(a, b):
    '''각 단어의 갯수를 파악'''
    dic1 = {}
    dic2 = {}
    
    for i in list(a):
        if dic1.get(i) == None:
            dic1[i] = 1
        else:
            dic1[i] += 1

    for j in list(b):
        if dic2.get(j) == None:
            dic2[j] = 1
        else:
            dic2[j] += 1

    # print(dic1)
    # print(dic2)
    
    '''dic1 에서 dic2의 차이를 구해서, 서로 다른 문자의 갯수를 찾음'''
    for k in dic2.keys():
        if dic1.get(k) == None:
            dic1[k] = 0
        dic1[k] -= dic2[k]
        dic1[k] = abs(dic1[k])
    
    num = sum(dic1.values())
    return num

if __name__ == "__main__":
    a = input()
    b = input()
    ret = solution(a,b)
    print(ret)