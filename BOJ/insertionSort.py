
def insertionSort(arr):
    
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            # print(i, j)
            if arr[j] < arr[j-1]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

    print(arr)

if __name__ == "__main__":
    arr = [9,3,5,7,1,8,0]

    insertionSort(arr)