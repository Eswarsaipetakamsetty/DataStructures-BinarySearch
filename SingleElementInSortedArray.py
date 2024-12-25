"""(even, odd) if element is on right half
    (odd, even) if element is on left half"""

def singleElement(arr):
    n = len(arr)
    if len(arr) == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n-1] != arr[n-2]:
        return arr[n]
    
    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        
        if (mid %2 == 1 and arr[mid] == arr[mid - 1]) or (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
            low = mid + 1   #eliminate left half
        else:
            high = mid - 1 #eliminate right half
    return -1