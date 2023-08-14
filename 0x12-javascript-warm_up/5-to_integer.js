#!/usr/bin/node

// Get the number from the terminal
const arg = process.argv[2];

// Convert the number into an integer
const num = parseInt(arg);

// Print using console.log(...) if num arg is int
if (!isNaN(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
