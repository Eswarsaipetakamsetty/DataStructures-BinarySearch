
class Solution:
    def search(self,arr,key):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == key:
                return mid
            if arr[low] <= arr[mid]:
                if arr[low] <= key and key <= arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if arr[mid] <= key and key <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1



if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))
        print("~")
