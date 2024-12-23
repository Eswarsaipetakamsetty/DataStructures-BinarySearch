def binarySearch(arr, n, target):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


#binary search recursive

def binarysearchrec(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) / 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarysearchrec(arr, low, mid-1, target)
    else:
        return binarysearchrec(arr, mid+1, high, target)