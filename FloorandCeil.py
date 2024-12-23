#floor is largest no that is <= x
#ceil is smallest no that is >= x

#ceil is nothing but lowerbound

def floor(arr, target):
    n = len(arr)
    result = -1 
    low = 0
    high = n - 1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] <= target:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return arr[result]