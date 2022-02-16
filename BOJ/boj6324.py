
'''
    문제에 주어진 조건대로 split하여 해결
    포트와 패스 포함여부를 ':','/' 문자를 가지고 하였는데,
    패스뒤에 포트가 오는 경우, 예외처리를 하여
    포트를 default로 출력해주어야함
'''

def solution(URL):

    protocol = ''
    host = ''
    port = '<default>'
    path = '<default>'

    sub_URL = URL.split('://',1)
    if sub_URL[0] in ['http', 'ftp', 'gopher']:
        protocol = sub_URL[0]
    
    # print("[check] ", list(sub_URL[1]))
    # print("[check] ", ':' in list(sub_URL[1]) and '/' in list(sub_URL[1]))
    if ':' in list(sub_URL[1]) and '/' in list(sub_URL[1]):
        if list(sub_URL[1]).index(':') < list(sub_URL[1]).index('/'):
            host = sub_URL[1].split(':',1)[0]
            port = sub_URL[1].split(':',1)[1].split('/',1)[0]
            path = sub_URL[1].split(':',1)[1].split('/',1)[1]
        else: ## 포트번호가 뒤에 오는 경우, 예외처리를 해줘야함
            host = sub_URL[1].split('/',1)[0]
            path = sub_URL[1].split('/',1)[1]
    
    

    elif ':' in list(sub_URL[1]) or '/' in list(sub_URL[1]):
        if ':' in list(sub_URL[1]):
            host = sub_URL[1].split(':',1)[0]
            port = sub_URL[1].split(':',1)[1]
        
        if '/' in list(sub_URL[1]):
            host = sub_URL[1].split('/',1)[0]
            path = sub_URL[1].split('/',1)[1]
    
    else:
        host = sub_URL[1]

    return protocol, host, port, path
    
    
if __name__ == "__main__":
    TC = int(input())
    for idx in range(TC):
        URL = input()
        
        protocol, host, port, path = solution(URL)
        
        print("URL #{}" .format(idx+1))
        print("Protocol = {}" .format(protocol))
        print("Host     = {}" .format(host))
        print("Port     = {}" .format(port))
        print("Path     = {}" .format(path))
        print()
        
