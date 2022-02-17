'''
입력 : 
41
0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 0
1
1 1

출력 : 
1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 
1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 
1
'''

def solution(switch, std_arr):
    size = len(switch)

    for gender, swt_num in std_arr:
        if   gender == 1:   # 남자인 경우, 배수와 같은 번호의 스위치 상태 변경
            for idx in range(swt_num-1, size, swt_num):
                switch[idx] = 0 if switch[idx] == 1 else 1
        elif gender == 2:   # 여자인 경우, 좌우로 확장하면서 대칭이 맞는 스위치의 상태 변경
            dist = 0
            switch[swt_num-1] = 0 if switch[swt_num-1] == 1 else 1
            while(True):
                dist = dist + 1
                lidx = swt_num - dist
                ridx = swt_num + dist
                # print("[check] ", lidx-1, ridx-1)
                if 0 <= lidx-1 and ridx-1 < size:
                    if switch[lidx-1] == switch[ridx-1]:
                        switch[lidx-1] = 0 if switch[lidx-1] == 1 else 1
                        switch[ridx-1] = 0 if switch[ridx-1] == 1 else 1
                    else:
                        break
                else:
                    break
    
    for i in range(size):
        print(str(switch[i]), end = '')
        if i == size-1: ## 마지막에 개행
            print()
        else:
            print(' ', end='')

        if i != 0 and (i+1) % 20 == 0: ## 20개씩 개행
            print()
        

if __name__ == "__main__":
    TC = int(input())
    switch = list(map(int, input().split()))
    std_num = int(input())
    std_arr = []
    for _ in range(std_num):
        std_arr.append(list(map(int, input().split())))

    solution(switch, std_arr)