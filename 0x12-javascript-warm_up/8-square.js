#!/usr/bin/node

// Get the square size from the user
const size = process.argv[2];

// Convert the argument into a number
const num = parseInt(size);

// Check if conversion is successful an +eve
if (!isNaN(num) && num > 0) {
  for (let i = 1; i <= num; i++) {
    let row = '';
    for (let j = 1; j <= num; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
