'''Smallest index such that arr[index] >= x'''

def lowerBound(arr, target):
    n = len(arr)
    result = n
    low = 0
    high = n - 1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] >= target:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result


#smalles index such that arr[index] > x
def upperBound(arr, target):
    n = len(arr)
    result = n
    low = 0
    high = n - 1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] > target:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result

print(lowerBound([1, 3, 3, 5, 77, 3], 2))
