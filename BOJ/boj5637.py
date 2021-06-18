'''
    주어진 문자열에 단어를 뽑아내야함.
    aaa.bbbb 의 경우 'aaa', 'bbbb' 가 단어가 된다. 
'''

if __name__ == "__main__":
    arr = []
    end_flag = 0
    while(end_flag == 0):
        strings = input().split()

        for ss in strings:
            if ss == 'E-N-D':
                end_flag = 1
                break

            tmp = ""
            for s in ss:
                if s.isalpha() or s == '-':
                    tmp += s
                    continue
                else:
                    if len(tmp) > 0:
                        arr.append(tmp)
                        tmp = ""
            else:
                if len(tmp) > 0:
                    arr.append(tmp)
    # print(arr)
    

    length = list(map(len, arr))
    # print(length)

    max_idx = length.index(max(length))
    print(arr[max_idx].lower())