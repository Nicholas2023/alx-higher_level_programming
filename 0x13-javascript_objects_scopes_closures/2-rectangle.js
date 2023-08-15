#!/usr/bin/node

// Class Rectangle defined
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
    } else if (w === undefined || h === undefined) {
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

// Export the module
module.exports = Rectangle;
