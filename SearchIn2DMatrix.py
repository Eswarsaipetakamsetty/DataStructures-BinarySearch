"""formula 
    ind / n => row
    ind % n => col
"""
def search2DMatrix(arr, k):
    low = 0
    m = len(arr)
    n = len(arr[0])
    high = len(arr)* len(arr[0]) - 1
    while low <= high:
        mid = (low + high) // 2
        row = mid // n
        col = mid % n
        if arr[row][col] == k:
            return True
        elif arr[row][col] < k:
            low = mid + 1
        else:
            high = mid - 1

    return False

