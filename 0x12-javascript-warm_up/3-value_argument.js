#!/usr/bin/node

// Get the first argument from the terminal
const firstArg = process.argv[2];

// Printing the arguments using console.log(...)
if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
