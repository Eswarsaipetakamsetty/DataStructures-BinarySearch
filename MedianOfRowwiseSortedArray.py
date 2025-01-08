def Median(arr):
    m = len(arr)
    n = len(arr[0])
    low = float('inf')
    high = -float('inf')
    for i in range(m):
        low = min(low, arr[i][0])
        high = max(high, arr[i][m - 1])
    req = (m * n) // 2
    while low <= high:
        mid = (low + high) // 2
        ctr = smallEquals(arr, m, n, mid)
        if ctr <= mid: low = mid + 1
        else:   high = mid - 1
    return low

def smallEquals(arr, m, n, x):
    ctr = 0
    for i in range(m):
        ctr += lowerBound(arr[i], x, n)
    return ctr
def lowerBound(arr, x, n):
    low = 0 
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans