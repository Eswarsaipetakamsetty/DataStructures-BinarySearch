def isPossible(arr, day, m, k):
    ctr = 0
    nbk = 0
    for i in range(len(arr)):
        if arr[i] <= day:
            ctr += 1
        else:
            nbk += (ctr//k)
            ctr = 0
    nbk += ctr//k
    if nbk >= m:
        return True
    return False
def mindays(arr, m, k):
    if len(arr) < m*k:
        return -1
    ans = high
    low = min(arr)
    high = max(arr)
    while low <= high:
        mid = (low + high) // 2
        if isPossible(arr, mid, m, k):
            high = mid - 1
            ans = mid
        else:
            low = mid + 1
    return ans
