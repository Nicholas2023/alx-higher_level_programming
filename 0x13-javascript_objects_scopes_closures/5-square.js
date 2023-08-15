#!/usr/bin/node

// Import the 4-rectangle file
const Rectangle = require('./4-rectangle');

// Define class Square with inherited properties
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

// Export the module
module.exports = Square;
