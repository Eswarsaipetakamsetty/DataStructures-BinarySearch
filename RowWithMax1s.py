def lowerBound(arr, n, k):
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= k:
            ans = mid
            high = mid - 1
        else:   low = mid + 1
    return ans
def rowWithMax1s(arr, n, m):
    ctrmax = 0
    ind = -1
    for i in range(n):
        ctr =   m -  lowerBound(arr[i], m, 1)
        if ctr > ctrmax:
            ctrmax = ctr
            ind = i
    return ind