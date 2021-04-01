N = int(input())
M = int(input())
S = str(input())


'''
# 3개씩 잘라서 갯수를 비교하는 방법 -> 시간초과 발생

p1 = "I"
for i in range(0,N):
    p1 += "OI"

print(p1)

hash = {}
for i in range(0, len(S)-len(p1)+1):
    text = S[i:i+len(p1)]
    if text not in hash:
        hash[text] = 1
    else:
        hash[text] += 1

print(hash)
print(hash[p1])

answer = 0
for i in range(0, len(S)-len(p1)+1):
    text = S[i:i+len(p1)]
    if text == p1:
        answer += 1
'''

answer = 0
idx = 0
while( idx < M ):
    if( S[idx:idx+2] == 'IO' ):
        # print(S[idx:idx+2], idx)
        num = 0
        while( S[idx+1:idx+3] == 'OI' ):
            # print(S[idx+1:idx+3], idx)
            num += 1
            idx += 2
            if( num == N ):
                num -= 1
                answer += 1
    idx += 1


print(answer)
    
