def solution(N):
    answer = 0
    binary = bin(N).lstrip('0b')
    print(binary)

    answer_list = []
    idx = -1

    # 1을 찾아 거리를 계산
    for i in range(0, len(binary)):
        if binary[i] == '1':
            if idx == -1:
                idx = i
            else:
                answer_list.append(i-idx-1)
                idx = i


    if (len(answer_list) != 0):
        answer = max(answer_list)
    return answer
