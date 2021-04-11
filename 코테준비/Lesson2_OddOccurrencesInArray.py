'''
    A의 원소를 셋에 넣어 중복을 제거한 후
    해당 원소가 A에서 홀수개를 가진다면 리턴.
    
    결과 : Taskscore : 66% / Correctness : 100% / Performance : 26%

def solution(A):
    answer = 0

    num_set = set()

    for number in A:
        num_set.add(number)
    
    for i in list(num_set):
        if( A.count(i) % 2 != 0 ):
            answer = i
    
    return answer

'''

'''
    리스트를 한번 순회할 때, 딕셔너리에 키와 갯수를 저장하여
    홀수개를 가진 key를 리턴한다.
'''
def solution(A):
    answer = 0

    dic = {}
    # A의 원소와 그 갯수를 딕셔너리에 저장
    for i in A:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1

    for key in list(dic):
        if( dic[key] % 2 != 0):
            answer = key

    return answer