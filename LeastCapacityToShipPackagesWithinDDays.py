def check(arr, cap, days):
    load = 0
    day = 1
    for i in range(len(arr)):
        if load + arr[i] > cap:
            day += 1
            load = arr[i]
        else:
            load += arr[i]
    if day <= days:
        return True
    return False
def leastCapacity(arr, days):
    low = max(arr)
    high = sum(arr)
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            high = mid - 1
        else:
            low = mid + 1
    return low
    