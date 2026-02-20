def kth_smallest(arr, k):
    arr.sort()          # sort the array
    return arr[k - 1]   # k-th smallest (1-based index)

# Example
arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4
print(kth_smallest(arr, k))