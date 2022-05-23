// Iterative
function factorialIterative(num) {
  let fact = 1;
  for (let i = 2; i <= num; i++) {
    fact = fact * i;
  }
  return fact;
}

console.log(factorialIterative(0)); // 1
console.log(factorialIterative(5)); // 120
console.log(factorialIterative(8)); // 40320

// Recursive
function factorialRecursive(num) {
  if (num === 0) {
    return 1;
  } else {
    return num * factorialRecursive(num - 1);
  }
}

console.log(factorialRecursive(0)); // 1
console.log(factorialRecursive(5)); // 120
console.log(factorialRecursive(8)); // 40320

// Big-O = O(n)
