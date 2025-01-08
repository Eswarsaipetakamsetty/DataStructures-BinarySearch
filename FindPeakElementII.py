def findPeak(mat):
    m = len(mat)
    n = len(mat[0])
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        row = maxRow(mat, m, n, mid)
        left = mat[row][mid - 1] if mid - 1 >= 0 else -1
        right = mat[row][mid + 1] if mid + 1 < n else -1
        if mat[row][mid] > left and mat[row][mid] > right:
            return [row, mid]
        elif mat[row][mid] < left:  high = mid -1 
        else:   low = mid + 1
    return [-1, -1]

def maxRow(a, m, n, col):
    maxele = -1
    maxind = -1
    for i in range(m):
        if a[i][col] > maxele:
            maxele = a[i][col]
            maxind = i
    return maxind
