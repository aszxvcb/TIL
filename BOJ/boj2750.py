# 수 정렬하기

N = int(input())
arr = []
for idx in range(0, N):
    arr.append(int(input()))
    
arr.sort()

for num in arr:
    print(num)