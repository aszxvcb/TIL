def solution(n):
    answer = 0
    s = []

    while( n >= 1):
        s.append(str(int(n%3)))
        n /= 3

    s.reverse()

    for i in range(0, len(s)):
        answer += pow(3,i) * int(s[i])

    return answer


if __name__ == "__main__":
    ret = solution(45)
    print(ret)