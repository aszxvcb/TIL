# 수 정렬하기
# 머지소트

def mergesort(arr):
    # mergesort
    # print(arr)

    if (arr is None) or (len(arr) <= 1):
        return arr

    # 배열을 반반씩 나눈다.
    mid_idx = len(arr)//2
    left_arr = arr[:mid_idx]
    right_arr = arr[mid_idx:]

    left_arr = mergesort(left_arr)
    right_arr = mergesort(right_arr)

    # print("left : ", left_arr)
    # print("right : ", right_arr)

    # 두 배열을 정렬하면서 병합
    sorted_arr = []
    left_idx = 0; right_idx = 0
    while(left_idx < len(left_arr) and right_idx < len(right_arr)):
        if( left_arr[left_idx] <= right_arr[right_idx] ):
            sorted_arr.append(left_arr[left_idx])
            left_idx+=1
        else:
            sorted_arr.append(right_arr[right_idx])
            right_idx+=1

    # 한쪽의 배열이 다 정렬되었다면, 남은 배열의 인덱스를 모두 뒤로 이어 붙인다.
    if left_idx == len(left_arr):
        sorted_arr.extend(right_arr[right_idx:])
    elif right_idx == len(right_arr):
        sorted_arr.extend(left_arr[left_idx:])
    
    # print("sorted : ", sorted_arr)
    return sorted_arr

if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))

    # arr = [10,9,8,7,6,5,4,3,2,1]

    ret = mergesort(arr)

    for elem in ret:
        print(elem)
