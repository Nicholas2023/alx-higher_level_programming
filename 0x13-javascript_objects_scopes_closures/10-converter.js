#!/usr/bin/node

// Function definition and export
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
