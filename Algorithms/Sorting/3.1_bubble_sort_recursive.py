# Python code for recursive bubble sort
def bubble_sort(arr, n):

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    # Recursively calling function if length of array greater than 1
    if n - 1 > 1:
        bubble_sort(arr, n - 1)

# Sample array for sorting
arr = [5, 3, 8, 1, 9, 6]
print(f"Array before sorting : {arr}")

# Calling function
bubble_sort(arr, len(arr))
print(f"Array after sorting : {arr}")
