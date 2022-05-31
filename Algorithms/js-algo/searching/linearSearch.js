function linearSearch(arr, target) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == target) {
      return i
    }
  }
  return -1
}

console.log(linearSearch([4, 1, 6, 3, 9], 6)) // 2
console.log(linearSearch([-3, -1, -4], -3)) // 0
console.log(linearSearch([7, 5, 3, 9], 10)) // -1

// Big-O = O(n)
