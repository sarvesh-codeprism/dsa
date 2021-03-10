# Python code to search element 'x' in array 'arr' of length 'n' by linear search

def linear_search(arr, n, x):
    for ind in range(n):
        if arr[ind] == x:
            return ind
    return -1

arr = [1, 2, 3, 4]
n = len(arr)
x = int(input(f'Enter a number to search in {arr} : '))

# Calling function
result = linear_search(arr, n, x)

if result == -1:
    print(f'Element {x} is not present in {arr}')
else:
    print(f'Element {x} is present at index {result} in {arr}')
