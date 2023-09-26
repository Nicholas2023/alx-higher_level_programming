#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the movie Id from the command-line arguments
const movieId = process.argv[2];

// Define the URL to the Star Wara API with the movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the specified URL
request(url, (error, response, body) => {
  if (error) {
    // If an error occurs during the request, print the error
    console.error(error);
  } else {
    // Parse the JSON response to extract the movie title
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
