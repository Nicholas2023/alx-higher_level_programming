#!/usr/bin/node
const data = require('./101-data');
const dict = data.dict;

const reversedDict = {};

for (const userId in dict) {
  const occurrences = dict[userId];
  if (reversedDict[occurrences] === undefined) {
    reversedDict[occurrences] = [];
  }
  reversedDict[occurrences].push(userId);
}

console.log(reversedDict);
