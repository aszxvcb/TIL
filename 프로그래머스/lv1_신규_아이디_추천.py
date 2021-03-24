
'''
    python 에서의 substring 은 [:] 슬라이싱으로 가능
    이때 뒤에오는 인자의 전 인덱스까지 수행함

    그리고 슬라이싱은 아웃오브인덱스를 검사하지 않음.
    범위를 벗어날 경우는 무시함

    str = "12345"
    str = str[-99:9]
    print(str) # 12345 출력

    풀이 후 답안을 확인하니, 정규표현식을 사용하면 쉽게 해결이 가능...
  
    import re

    def solution(new_id):
        st = new_id
        st = st.lower()
        st = re.sub('[^a-z0-9\-_.]', '', st)
        st = re.sub('\.+', '.', st)
        st = re.sub('^[.]|[.]$', '', st)
        st = 'a' if len(st) == 0 else st[:15]
        st = re.sub('^[.]|[.]$', '', st)
        st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
        return st
        
'''

def solution(new_id):
    answer = ''

    new_id = new_id.lower()

    for char in new_id:
        if( char.isdigit() or char.isalpha() or char == '-' or char == '_' or char == '.' ):
            continue
        else:
            new_id = new_id.replace(char, '')

    while( new_id.find("..") != -1 ):
        new_id = new_id.replace("..", ".")

    if( new_id[0] == '.'):
        new_id = new_id[1:]
    if( len(new_id) >= 1 and new_id[-1] == '.'):
        new_id = new_id[0:-1]

    if( len(new_id) == 0 ):
        new_id = 'a'
    
    if( len(new_id) >= 16 ):
        new_id = new_id[0:15]
        if( new_id[-1] == '.' ):
            new_id = new_id[0:-1]
    
    while( len(new_id) < 3 ):
        new_id += new_id[-1]

    answer = new_id
    return answer

if __name__ == "__main__":

    new_id = "abcdefghijklmn.p"
    ret = solution(new_id)
    print(ret)