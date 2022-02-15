'''
    1. 기타 조합을 구한다.
    2. 기타 조합으로 연주가능한 음악의 수를 구한다.
    3. 연주가능한 음악의 최대값을 구한다.
'''

from itertools import combinations

def solution(dic):
    max_song = 0
    max_guitar = 0

    for i in range(1,N+1):
        comb = list(combinations(dic.keys(), i))
        for elem_set in comb:

            ## 연주가능한 음악을 계산한다.
            song_arr = ['N'] * M
            for elem in elem_set:
                for idx in range(M):
                    if song_arr[idx] == 'N' and dic[elem][idx] == 'Y':
                        song_arr[idx] = 'Y'

            ## 연주가능한 음악의 수를 센다.
            song_cnt = song_arr.count('Y')
            if song_cnt == M:
                return i
            elif song_cnt > max_song:
                max_song = song_cnt
                max_guitar = i
            

    if max_song == 0:
        return -1
    else:
        return max_guitar                   

if __name__ == "__main__":
    global N, M
    N, M = map(int, input().split())
    dic = {}
    for _ in range(N):
        guitar, song = input().split()
        dic[guitar] = list(song)
    
    result = solution(dic)
    print(result)
    