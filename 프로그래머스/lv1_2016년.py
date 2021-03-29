def solution(a, b):
    answer = ''

    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]

    month_a = [1,2,3,4,5,6,7,8,9,10,11,12]
    month_b = [31,29,31,30,31,30,31,31,30,31,30,31]

    for a in range(a-1, 0, -1):
        if a in month_a:
            b += month_b[ month_a.index(a) ]

    return day[b % 7]


if __name__ == "__main__":

    a = 2
    b = 1
    ret = solution(a,b)

    print( ret )