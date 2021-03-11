# Python code for recursive binary search
def binary_search(arr, x):
    # base case
    if len(arr) == 0:
        return False
    else:
        mid = len(arr)//2
        if arr[mid] == x:
            return True
        else:
            if x < arr[mid]:
                return binary_search(arr[: mid], x)
            else:
                return binary_search(arr[mid + 1 :], x)
# Sorted array for binary search
arr = [1, 2, 3, 4, 5]
x = int(input(f"Enter number to search in {arr} : "))

# Calling function
result = binary_search(arr, x)

if result == True:
    print(f"{x} is present in {arr}")
else:
    print(f"{x} is not present in {arr}")
