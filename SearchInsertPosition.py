def searchInsertPosition(arr, target):
    low = 0
    high = len(target) - 1
    result = len(target)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result

"""Same as lower bound"""