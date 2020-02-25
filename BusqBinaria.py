def binarySearch(arr, first, last, key):
    if (last >= first):
        mid = first + (last - first) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            return binarySearch(arr, first, mid-1, key)
        else:
            return binarySearch(arr, first, mid+1, key)
    return -1

arr = [10, 20, 30, 40, 50]
key = 30
last = len(arr) - 1
result = binarySearch(arr, 0, last, key)
if(result == -1):
    print("Element is not find")
else:
    print("Element is found at index: ", result)
