#!/usr/bin/node
// Importing the 5-square file
const BaseSquare = require('./5-square');

// Defining class Square with inheritance from Square
class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

// Export the module
module.exports = Square;
