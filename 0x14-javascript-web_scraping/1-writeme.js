#!/usr/bin/node

// Import the 'fs' module to work with file system operation
const fs = require('fs');

// Get the file path and string to write from command-line args
const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Write the content to the file in UTF-8 encoding
fs.writeFile(filePath, contentToWrite, 'utf-8', (error) => {
  if (error) {
    // If an error occurs during writing, print the error obj
    console.error(error);
  }
});
