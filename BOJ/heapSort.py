def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    
    return quickSort(lesser_arr) + equal_arr + quickSort(greater_arr)

if __name__ == "__main__":
    arr = [9,3,5,7,1,8,0]

    ret = quickSort(arr)
    print(ret)