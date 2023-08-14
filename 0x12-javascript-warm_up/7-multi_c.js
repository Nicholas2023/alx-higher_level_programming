#!/usr/bin/node

// Get the number of times to print the string
const numTimes = process.argv[2];

// Convert the argument to an integer
const num = parseInt(numTimes);

// Check if the argument is an int the print
if (!isNaN(num)) {
  for (let i = 1; i <= num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
