def check(arr, n, mid):
    stu = 1
    pages = 0
    for i in range(n):
        if pages + arr[i] <= mid:
            pages += arr[i]
        else:
            stu += 1
            pages = arr[i]
    return stu

def findPages(arr: list[int], n: int, m: int) -> int:
    if m > n:
        return -1
    low = max(arr)
    high = sum(arr)
    while low <= high:
        mid = (low + high) // 2
        res = check(arr, n, mid)
        if res > m:
            low = mid + 1
        else:
            high = mid - 1
    return low

