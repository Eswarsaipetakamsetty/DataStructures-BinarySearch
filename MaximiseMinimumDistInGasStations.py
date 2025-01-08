"""bruteforce code"""

def minimise(arr, k):
    n = len(arr)
    howmany = [0 for _ in range(n-1)]
    for gs in range(k):
        maxsection = -1
        maxind = -1
        for i in range(n-1):
            diff = arr[i + 1] - arr[i]
            sectionlength = diff/(howmany[i] + 1)
            if sectionlength > maxsection:
                maxsection = sectionlength
                maxind = i
        howmany[maxind] += 1
    maxans = -1
    for i in range(n-1):
        diff = arr[i + 1] - arr[i]
        sectionlength = diff/(howmany[i] + 1)
        maxans = max(maxans, sectionlength)
    return maxans

"""better"""

import  heapq
def minimuseWithPriorityQueue(arr, k):
    n = len(arr)
    howMany = [0]*(n - 1)
    pq = []
    for i in range(n-1):
        heapq.heappush(pq, (arr[i+1] - arr[i] , i))
    for _ in range(1, k+1):
        tp = heapq.heappop(pq)
        secInd = tp[1]
        howMany[secInd] += 1
        inDiff = arr[secInd + 1] - arr[secInd]
        newSecLen = inDiff / (howMany[secInd] + 1)
        heapq.heappush(pq, (newSecLen, secInd))
    return pq[0][0]
    
"""optimal solution"""
def noOfGasStations(arr, dist):
    ctr = 0
    for i in range(1, len(arr)):
        numberInBetween = (arr[i] - arr[i - 1])//dist
        if(arr[i] - arr[i-1])/dist == numberInBetween*dist:
            numberInBetween -= 1
        ctr += numberInBetween
    return ctr
def minimised(arr, k):
    low = 0
    n = len(arr)
    high = -1
    for i in range(n-1):
        if high < arr[i+1] - arr[i]:
            high = arr[i+1] - arr[i]
    diff = 1e-6
    while low - high > diff:
        mid = (low + high) / (2.0)
        ctr = noOfGasStations(arr, mid)
        if ctr > k:
            low = mid
        else:
            high = mid
    return high

