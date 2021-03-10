# Python code for iterative binary search

def binary_search(arr, x):
    first = 0
    last = len(arr) - 1
    found = False
    # cheacking base case
    while first <= last and not found:
        mid = (first + last) // 2
        if arr[mid] == x:
            found = True
        else:
            if x < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found
# sorted array for binary search
arr = [10, 20, 30, 40]
x = int(input(f'Enter element to search in {arr} : '))

# calling function
result = binary_search(arr, x)

if result:
    print(f'{x} is present in {arr}')
else:
    print(f'{x} is not present in {arr}')
