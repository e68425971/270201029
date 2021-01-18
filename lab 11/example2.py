def BinarySearch(arr, low, high, x):
    [5]
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return BinarySearch(arr, low, mid - 1, x)
        else:
            return BinarySearch(arr, mid + 1, high, x)
    else:
        return -1

