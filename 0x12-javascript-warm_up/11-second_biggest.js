#!/usr/bin/node
// Get the arguments passed to the script
const args = process.argv.slice(2);

// Convert the args to ints an sort them(descending)
const list = args.map(Number).sort((a, b) => b - a);

// Check the length of the sorted arrays to determine output
if (list.length === 0 || list.length === 1) {
  console.log(0);
} else {
  console.log(list[1]);
}
