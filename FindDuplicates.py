def findDuplicates(arr):
    low = 1
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        ctr = 0
        for i in arr:
            if i <= mid:
                ctr += 1
        if ctr > mid:
            high = mid - 1
        else:
            low = mid + 1
    return low