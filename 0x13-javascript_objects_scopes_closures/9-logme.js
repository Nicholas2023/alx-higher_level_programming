#!/usr/bin/node

// Global variable
let count = 0;
// Function definition and export
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
