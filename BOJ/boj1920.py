n = input()
A = input().split()

n = input()
B = input().split()

dic = {x:0 for x in A}
print(dic)

for num in B:
    if num in dic:
        print(1)
    else:
        print(0)