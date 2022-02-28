from itertools import combinations

# 거리두기 확인하기
'''
    1. 입력받은 배열에서 응시자의 위치를 구함
    2. 응시자들의 위치조합에서 맨하튼거리를 구함
    3. 맨하튼거리가 2인 경우, 둘 사이에 파티션이 존재하는지 추가확인
'''

def solution(places):
    result = []

    for room in places:
        P = []
        flag = True
        for row, line in enumerate(room):
            for col, elem in enumerate(line):
                if "P" == elem: ## 응시자들의 위치를 구함
                    P.append([row, col])

        ## 응시자들의 거리를 계산
        comb = list(combinations(P, 2))
        for elem in comb:
            ## 맨하튼거리 |r1 - r2| + |c1 - c2|
            r1, c1 = elem[0]
            r2, c2 = elem[1]
            dist = abs(r1 - r2) + abs(c1 - c2)
            if dist == 2:
                print(elem, dist)

                ## 파티션으로 막혀있는 경우 skip
                ### 같은 행 또는 같은 열에 앉은 경우
                if r1 == r2:
                    mid = ((c1 + c2) // 2)
                    print( r1, mid , room[r1][mid])
                    if room[r1][mid] != 'X':
                        flag = False

                elif c1 == c2:
                    mid = ((r1 + r2) // 2)
                    print( mid, c1 , room[mid][c1])
                    if room[mid][c1] != 'X':
                        flag = False
                
                else: ### 대각선으로 앉은 경우
                    if not (room[r1][c2] == 'X' and room[r2][c1] == 'X'):
                        flag = False

            elif dist == 1:
                flag = False


        result.append(1) if flag == True else result.append(0)
    return result

if __name__ == "__main__":

    # print( solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]]) )

    #TC1
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],\
              ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],\
              ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],\
              ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],\
              ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    result = [1, 0, 1, 1, 1]
    assert solution(places) == result
