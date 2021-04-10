''' 
    import math 를 추가하여 ceil() 함수를 사용하면
    더 쉽게 구할 수 있을 것 같음
'''

# X에 D를 더해 Y를 넘기거나 같은수를 만드는 덧셈의 횟수구하기
def solution(X, Y, D):
    answer = 0

    distance = Y - X
    count = distance / D
    rem = distance % D

    if rem != 0:
        count += 1
    
    answer = int(count)
    return answer