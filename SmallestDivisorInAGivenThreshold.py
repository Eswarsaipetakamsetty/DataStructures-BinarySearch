import math
def check(arr, n, th):
    res = 0
    for i in range(len(arr)):
        res += math.ceil(arr[i]/n)
    if res <= th:
        return True
    return False

def SmallestDivisor(arr, th):
    low = 1
    high = max(arr)
    while low <= high:
        mid = (low + high) // 2
        if check(arr,mid, th):
            high = mid - 1
        else:
            low = mid + 1
    return low   #opposite polarity

        
