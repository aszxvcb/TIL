'''
    - 중복을 고려하기 위해 set 자료구조 사용

    문제에 알고리즘 유형에는 비트마스킹이 들어가 있는데, set을 이용한 풀이도 가능한 것 같음
'''

import sys

if __name__ == "__main__":
    M = int(input())
    
    my_set = set()

    for _ in range(M):
        cmd = sys.stdin.readline().rstrip()
        
        if cmd == 'all':
            my_set = set([i for i in range(1,21)])
        elif cmd == 'empty':
            my_set = set()
        else:
            cmd, value = cmd.split()
            value = int(value)

            if cmd == 'add':
                my_set.add(value)
            elif cmd == 'remove':
                try:
                    my_set.remove(value)
                except KeyError:
                    continue
            elif cmd == 'check':
                if value in my_set:
                    print(1)
                else:
                    print(0)
            elif cmd == 'toggle':
                try:
                    my_set.remove(value)
                except KeyError:
                    my_set.add(value)
        