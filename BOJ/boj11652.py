'''
    해시테이블을 이용하여 입력받은 수를 카운트 함
    입력된 키들의 값을 비교하여 정답을 도출

    - key를 입력받을 때, 정수형으로 입력받는 것이 중요
    key = int(sys.stdin.readline().rstrip())
    문자열로 받을 때 음수연산이 제대로 되지 않음

    반례
    6
    -3
    -2
    -1
    0
    1
    2
'''

import sys, heapq

if __name__ == "__main__":
    N = int(input())
    
    dic = {}
    for _ in range(N):
        key = int(sys.stdin.readline().rstrip())
        
        if dic.get(key, None) == None:
            dic[key] = 1
        else:
            dic[key] += 1
    
    max_key = 0
    max_value = 0
    for key in dic.keys():
        if dic[key] > max_value:
            max_key = key
            max_value = dic[key]
        elif dic[key] == max_value:
            if key < max_key:
                max_key = key
        
    print(max_key)