# 숫자 문자열과 영단어
'''
    1. 딕셔너리 맵핑
'''

def solution(s):
    eng_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

    for eng in eng_dic.keys():
        s = s.replace( eng, eng_dic[eng], s.count(eng))
        
    return int(s)

if __name__ == "__main__":

    #TC1
    s = "one4seveneight"
    result = 1478
    assert solution(s) == result
    
    #TC2
    s = "23four5six7"
    result = 234567
    assert solution(s) == result

    #TC3
    s = "2three45sixseven"
    result = 234567
    assert solution(s) == result

    #TC4
    s = "123"
    result = 123
    assert solution(s) == result