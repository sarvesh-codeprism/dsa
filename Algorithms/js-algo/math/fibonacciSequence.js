function fibonacci(num) {
  const fib = [0, 1];
  for (let i = 2; i < num; i++) {
    fib[i] = fib[i - 1] + fib[i - 2];
  }
  return fib;
}

console.log(fibonacci(2)); // [ 0, 1 ]
console.log(fibonacci(4)); // [ 0, 1, 1, 2 ]
console.log(fibonacci(6)); // [ 0, 1, 1, 2, 3, 5 ]

// Big-O = O(n)