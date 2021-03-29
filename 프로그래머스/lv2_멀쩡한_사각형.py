from math import gcd

def solution(w,h):
    answer = 1

    num = gcd(w, h)
    i = w/num
    j = h/num
    minus_block = i+j-1

    answer = w * h - (minus_block * num)

    return answer

if __name__ == "__main__":
    w = 6
    h = 10
    ret = solution(w,h)
    print(int(ret))