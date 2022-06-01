function binarySearch(arr, target) {
  let start = 0;
  let end = arr.length;
  // console.log(end)
  let mid;
  while (end >= start) {
    mid = Math.floor((start + end) / 2)
    console.log("Mid", mid)
    if (arr[mid] === target) {
      return mid;
    } else if (arr[mid] > target) {
      end = mid - 1
    } else if (arr[mid] < target) {
      start = mid + 1;
    }
  }
  return -1
}

console.log(binarySearch([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], -3)) // 2

// Big-O = O(logn)
