'''
행열을 어떤 단어로 표시했는지 잘봐야함.
N개의 줄에 M개 -> 행 N , 열 M
'''

def solution(arr):

    max = float('-INF')
    ret = -1
    
    # print(arr, len(arr), len(arr[0]))

    for col in range(len(arr[0])):
        num = 1     # reset value
        for row in range(len(arr)):
            num *= arr[row][col]    
            
        if max <= num:
            max = num
            ret = col
        # print(num)

    return ret+1


if __name__ == '__main__':

    T = int(input())
    
    for i in range(T):
        M, N = map(int, input().split())
        arr = []
        
        for j in range(N):
            arr.append(list(map(int, input().split())))
        print(solution(arr))


'''
1 2 3 4 5
5 4 3 2 1
5 5 5 5 5
[[1,2,3,4,5],
 [5,4,3,2,1],
 [5,5,5,5,5]]
'''