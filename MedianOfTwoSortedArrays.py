def MedianOfTwoSortedArrays(arr1, arr2):  #bruiteforce approach
    i = 0
    j = 0
    n1 = len(arr1)
    n2 = len(arr2)
    new = []
    while (i < n1 and j < n2):
        if arr1[i] < arr2[j]:
            new.append(arr1[i])
            i += 1
        else:
            new.append(arr2[j])
            j += 1
    while i < n1:
        new.append(arr1[i])
    while j < n2:
        new.append(arr2[j])

    n = n1 + n2
    if n%2!= 0:
        return new[(n+1)//2]
    else:
        return (new[n//2] + new[n//2 + 1])//2 
    
def MedianOfTwoSortedArrays(arr1, arr2):   #better space complexity
    n1 = len(arr1)
    n2 = len(arr2)
    n = n1 + n2
    ind1 = n//2
    ind2 = ind1 - 1
    ind1ele = ind2ele = -1
    i = j = ctr = 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            if ctr == ind1: ind1ele = arr1[i]
            if ctr == ind2: ind2ele = arr1[i]
            i += 1
            ctr += 1
        else:
            if ctr == ind1: ind1ele = arr1[j]
            if ctr == ind2: ind2ele = arr1[j]
            j += 1
            ctr += 1
    while i < n1:
        if ctr == ind1: ind1ele = arr1[i]
        if ctr == ind2: ind2ele = arr1[i]
        i += 1
        ctr += 1
    while j < n2:
        if ctr == ind1: ind1ele = arr1[j]
        if ctr == ind2: ind2ele = arr1[j]
        j += 1
        ctr += 1
    
    if n%2 != 0:
        return ind2ele
    return (ind1ele + ind2ele) // 2


def MedianOfTwoSoretdArrays(arr1, arr2):    #optimal solution
    n1 = len(arr1)
    n2 = len(arr2)
    if n1 > n2: return MedianOfTwoSoretdArrays(arr2, arr1)
    low = 0
    high = n1
    left = (n1+n2+1) // 2
    n = n1 + n2
    
    while low <= high:
        mid1 = (low + high) //2
        mid2 = left - mid1
        l1 = l2 = -float('inf')
        r1 = r2 = float('inf')
        if mid1 < n1:   r1 = arr1[mid1]
        if mid2 < n2:   r2 = arr2[mid2]
        if mid1 - 1 >= 0:   l1 = arr1[mid1 - 1]
        if mid2 - 1 >= 0:   l2 = arr2[mid2 - 1]
        if l1 <= r2 and l2 <= r1:
            if n%2 == 1:
                return max(l1, l2)
            return (max(l1 , l2) + min(r1, r2)) / 2
        elif l1 > r2:   high = mid1 - 1
        else:   low = mid1 + 1
    return 0
    