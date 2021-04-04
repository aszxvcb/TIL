def solution(brown, yellow):
    answer = []
    total = brown + yellow

    pair_list = []
    for width in reversed(range(1, total+1)):
        if ( total % width == 0 ):
            height = total / width
            if( width >= height ):
                pair_list.append((width, int(height)))
    print(pair_list)

    for pair in pair_list:
        width = pair[0]
        height = pair[1]

        if( (width+height-1)*2-2 == brown ):
            answer = pair

    return list(answer)

if __name__ == "__main__":
    ret = solution(10, 2)
    print(ret)