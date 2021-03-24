'''
    first, second, third 의 인덱스를 나머지연산을 통해 순환 함.

    enumrate 는 인덱스와, 값을 튜플로 같이 리턴한다.
'''

def solution(answers):
    answer = []

    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]

    score_list = []
    first_score = 0
    second_score = 0
    third_score = 0

    for idx in range (0, len(answers)):
        if( answers[idx] == first[idx%len(first)] ):
            first_score += 1
        if( answers[idx] == second[idx%len(second)] ):
            second_score += 1
        if( answers[idx] == third[idx%len(third)] ):
            third_score += 1
    
    score_list.append(first_score)
    score_list.append(second_score)
    score_list.append(third_score)

    print(score_list)
    max_num = max(score_list)

    # answer = [ idx+1 for idx, value in enumerate(score_list) if value == max_num ]
    # 아래와 같은 역할을 함
    
    for idx, value in enumerate(score_list):
        if( value == max_num):
            answer.append(idx+1)

    answer.sort()

    return answer

if __name__ == "__main__":
    answer = [1,3,2,4,2]
    ret = solution(answer)

    print(ret)