# Python code for bubble sort
def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(n - i - 1):
            # Swap if greater
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# sample array for sorting

arr = [2, 1, 7, 4, 9, 3, 5]
print(f"Array before sorting : {arr}")

# Calling function
bubble_sort(arr)

print(f"Array after sorting : {arr}")
