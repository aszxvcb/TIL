from itertools import permutations
from functools import cmp_to_key

'''
    비교함수 부분 참고!
'''

def compare(x, y):
    print( int(x+y), int(y+x))
    if( int(x+y) < int(y+x) ):
        return 1
    else:
        return -1

def solution(numbers):
    answer = ''

    numbers = list(map(lambda x: str(x), numbers))
    numbers.sort(key = cmp_to_key(compare))
    print(numbers)

    answer = "".join(numbers)

    answer = str(int(answer))

    return answer

""" # 순열로 접근하였으나, 시간초과 발생

    possible = list(permutations(numbers,len(numbers)))
    numbers = []
    for group in possible:
        group = list(map(lambda x : str(x), group))
        numbers.append( "".join(group))

    numbers = map(lambda x: int(x), numbers)
    answer = str(max(numbers))

    return answer
"""


if __name__ == "__main__":
    ret = solution([0,0,0,0,0])
    print(ret)