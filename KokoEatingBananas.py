import math
def totalhours(arr, n):
    result = 0
    for i in arr:
        result += math.ceil(i/n)
    return result

def minimumRateToEatBananas(arr, h):
    low = 1
    high = max(arr)
    while(low <= high):
        mid = (low + high) // 2
        total = totalhours(arr, mid)
        if total <= h:
            high = mid - 1
        else:
            low = mid + 1
    return low
    