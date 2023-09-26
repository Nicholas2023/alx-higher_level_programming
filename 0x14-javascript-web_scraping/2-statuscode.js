#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the URL to request from command-line arguments
const url = process.argv[2];

// Make a GET request to the specifies URL
request(url, (error, response) => {
  if (error) {
    // if an error occurs during the request, print the error
    console.error(error);
  } else {
    // Print the status code of the response
    console.log(`code: ${response.statusCode}`);
  }
});
