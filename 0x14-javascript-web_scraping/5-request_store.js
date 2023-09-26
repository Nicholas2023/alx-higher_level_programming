#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Import the 'fs' module to work with file system operations
const fs = require('fs');

// Get the URL and file path from command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request(url, (error, response, body) => {
  if (error) {
    // If an error occurs during the request, print the error
    console.error(error);
  } else {
    // Write the response body to the specified file in UTF-8 encoding
    fs.writeFile(filePath, body, 'utf-8', (writeError) => {
      if (writeError) {
        // If an error occurs while writing, print the error
        console.error(writeError);
      }
    });
  }
});
