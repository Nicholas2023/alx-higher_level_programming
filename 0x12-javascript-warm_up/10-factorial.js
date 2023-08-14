#!/usr/bin/node

// Function declaration and definition
function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n <= 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

// Get user input for number to compute
const num = parseInt(process.argv[2]);

// Compute factorial
const result = factorial(num);

// Print the results
console.log(result);
