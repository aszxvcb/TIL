# 신고 결과 받기
'''
    1. 중복제거
    2. 신고횟수가 k번 넘어가는지 체크
    3. 누가 신고했는지 체크
'''

from pprint import pprint

def solution(id_list, report, k):
    result = []
    id_dic = { id: { "cnt" : 0, "from" : [] } for id in id_list }
    
    ## 신고 건수 카운트
    for case in report:
        rprt_from, rprt_to = case.split()
        
        if rprt_from not in id_dic[rprt_to]["from"]:
            id_dic[rprt_to]["from"].append(rprt_from)
            id_dic[rprt_to]["cnt"] = id_dic[rprt_to]["cnt"] + 1
        
    # pprint(id_dic)

    ## 알림 대상 탐색
    result_dic = { id : 0 for id in id_list }
    for id in id_list:
        if id_dic[id]["cnt"] >= k:
            for rprt_from in id_dic[id]["from"]:
                result_dic[rprt_from] = result_dic[rprt_from] + 1

    for id in id_list:
        result.append(result_dic[id])

    return result


if __name__ == "__main__":

    #TC1
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2
    result = [2,1,1,0]

    assert solution(id_list, report, k) == result
    
    #TC2
    id_list = ["con", "ryan"]
    report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 3
    result = [0,0]

    assert solution(id_list, report, k) == result