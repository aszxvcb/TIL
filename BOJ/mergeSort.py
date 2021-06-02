def mergeSort(arr):
    if len(arr) < 2:
        return arr
    
    left = mergeSort(arr[0:len(arr)//2])
    right = mergeSort(arr[len(arr)//2:])

    # 병합
    merged = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1

    merged += left[l:]
    merged += right[r:]

    return merged

if __name__ == "__main__":
    arr = [9,3,5,7,1,8,0]

    ret = mergeSort(arr)
    print(ret)