
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # yntrum enq pivot
    pivot = arr[len(arr) // 2]

    left = []
    middle = []
    right = []

    # bajanum enq elementnery
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)

    # miavorum enq dasavorvac masery
    return quick_sort(left) + middle + quick_sort(right)


arr = [5, 2, 9, 1, 6]
print(quick_sort(arr))
