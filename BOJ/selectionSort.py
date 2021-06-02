
def selectionSort(arr):
    # print(arr)
    
    for i in range(len(arr)-1):
        min_val = arr[i]
        min_idx = i
        for j in range(i+1, len(arr)):
            # print(i, j)
            if min_val > arr[j]:
                min_idx = j
                min_val = arr[j]
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        # print(arr)
                
    print(arr)

if __name__ == "__main__":
    arr = [9,3,5,7,1,8,0]

    selectionSort(arr)