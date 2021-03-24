
def solution(numbers):
    answer = []

    s = set()

    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if( i != j ):
                s.add( numbers[i] + numbers[j] )

    answer = list(s)
    answer.sort()

    return answer


if __name__ == "__main__":

    numbers = [5,0,2,7]
    ret = solution(numbers)
    print(ret)