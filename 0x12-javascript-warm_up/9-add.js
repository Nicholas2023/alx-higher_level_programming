#!/usr/bin/node

// Function declaration and definition
function add (a, b) {
  return a + b;
}

// Get user arguments for addition
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

// Validate if arguments are integers
if (!isNaN(arg1) && !isNaN(arg2)) {
  const result = add(arg1, arg2);
  console.log(result);
} else {
  console.log('NaN');
}
