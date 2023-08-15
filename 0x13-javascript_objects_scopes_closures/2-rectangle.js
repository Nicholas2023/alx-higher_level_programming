#!/usr/bin/node

// Class Rectangle defined
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      // If any condition is met, an empty object is created
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

// Export the module
module.exports = Rectangle;
