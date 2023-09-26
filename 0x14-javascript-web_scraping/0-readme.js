#!/usr/bin/node

// Import the 'fs' module to work with file system operations
const fs = require('fs');

// Get the file path as a command-line argument
const filePath = process.argv[2];

// Read the content of the file in UTF-8 encoding
fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    // If an error occurs during reading, print the error object
    console.error(error);
  } else {
    // If reading is successful, print the content of the file
    console.log(data);
  }
});
