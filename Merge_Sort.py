def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # bajanum enq erku masi
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    # miavorum enq poqr elementneric sksac
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # avelacnum enq mnacac elementnery
    result += left[i:]
    result += right[j:]

    return result


arr = [5, 2, 9, 1, 6]
print(merge_sort(arr))
