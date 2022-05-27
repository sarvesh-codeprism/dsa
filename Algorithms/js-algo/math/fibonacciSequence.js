// Iterative : Finding sequennce
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

// Recursive : Finding nth fibonacci number
function fibonacciRecursive(num) {
  if (num === 0 || num === 1) {
    return num;
  }
  return fibonacciRecursive(num - 1) + fibonacciRecursive(num - 2);
}

console.log(fibonacciRecursive(2));
console.log(fibonacciRecursive(4));
console.log(fibonacciRecursive(6));

// Big-O = O(n)