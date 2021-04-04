# from itertools import permutations

# def solution(numbers):
#     answer = 0
#     numbers = list(map(lambda x: int(x), numbers))

#     ## 순열 이용 숫자 만들기
#     temp = []
#     for i in range(1, len(numbers)+1):
#         temp.extend(list(permutations(numbers,i )))
#     # print(temp)

#     permList = []
#     for i in range(0, len(temp)):
#         string = ""
#         for elem in temp[i]:
#             string += str(elem)
#         permList.append(string)
#     # print(permList)

#     numbers_set = set()
#     for number in permList:
#         numbers_set.add(int(number))
    
#     if( 0 in numbers_set ) : numbers_set.remove(0)
#     if( 1 in numbers_set ) : numbers_set.remove(1)
#     # print(numbers_set)

#     ## 소수 찾기
#     for elem in numbers_set:
#         for i in range(2, elem):
#             if( elem % i == 0):
#                 break
#         else:
#             # print("소수 : ", elem)
#             answer+=1

#     return answer


'''
    map을 이용하여 많은 코드로 만들었던 순열을 짧게 구현
    이후 에라토스테네스의 체를 이용하여 소수 제거
'''
from itertools import permutations

def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))

    for i in range(2, int(max(a) ** 0.5) + 1 ):
        a -= set(range(i*2, max(a) + 1, i))

if __name__ == "__main__":

    ret = solution("33")
    print(ret)