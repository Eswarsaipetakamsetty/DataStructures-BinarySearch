#min distance b/w any two cows

#maximum possible minimum distance


def check(arr, dist, cows):
    ctrcows = 1
    last = arr[0]
    for i in range(len(arr)):
        if arr[i] - last >= dist:
            ctrcows += 1
            last = arr[i]
    if ctrcows >= cows:
        return True
    return False


def aggressiveCows(stalls, k):
    stalls.sort()
    low = 0 
    high = stalls[-1] - stalls[0]
    while low <= high:
        mid = (low + high) // 2
        if check(stalls, mid, k):
            low = mid + 1
        else:
            high = mid - 1
    return high