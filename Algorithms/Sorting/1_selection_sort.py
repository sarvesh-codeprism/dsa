# Pyhton code for selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr

# Sample unsorted array
a = [2, 4, 1, 7, 5, 9, 8]
print(f"Original array : {a}")
# Calling function
result = selection_sort(a)

print(f"Sorted array : {result}")
