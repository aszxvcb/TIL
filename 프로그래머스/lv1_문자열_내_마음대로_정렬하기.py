def solution(strings, n):
    answer = []

    answer = sorted(strings, key = lambda x : [x[n], x])
    # strings.sort(key = lambda x: x[n]+x)
    '''
        key를 기준으로 sort 하도록 함
    '''

    return answer

if __name__ == "__main__":
    strings = ["abce", "abcd", "cdx"]
    n = 2
    ret = solution(strings, n)
    print(ret)