# Python code for merge sort
def merge_sort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2
		l = arr[:mid]
		r = arr[mid:]
		merge_sort(l)
		merge_sort(r)
		i = j = k = 0
		while len(l) > i and len(r) > j:
			if l[i] < r[j]:    	    	
				arr[k] = l[i]
				i += 1
			else:
				arr[k] = r[j]
				j += 1
			k += 1
   	     
		while len(l) > i:
			arr[k] = l[i]
			i += 1
			k += 1
		while len(r) > j:
			arr[k] = r[j]
			j += 1
			k += 1

	return arr

# sample array for sorting
a = [45, 34, 78, 12, 26, 63, 5]
print(f"Array before sorting : {a}")

# Calling function
result = merge_sort(a)
print(f"Sorted array : {result}")
