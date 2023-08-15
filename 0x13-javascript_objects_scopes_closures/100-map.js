#!/usr/bin/node
// File import
const data = require('./100-data');
const list = data.list;

// mapping of arrays
const newList = list.map((value, index) => value * index);

console.log(list);
console.log(newList);
