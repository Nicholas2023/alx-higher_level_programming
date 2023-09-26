#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the Movie ID from the command-line arguments
const movieId = process.argv[2];

// Define the URL to the Star Wars API for the movie with the given ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the specified URL
request(url, (error, response, body) => {
  if (error) {
    // If an error occurs during the request, print the error
    console.error(error);
  } else {
    // Parse the JSON response to extract the characters data
    const movieData = JSON.parse(body);

    // Create an array to store character URLs in the same order
    const characterUrls = movieData.characters;

    // Loop through chacracter URL and make requests to retrieve character names
    characterUrls.forEach((characterUrl) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          // If an error occurs during character request, print the error
          console.error(charError);
        } else {
          // Parse the JSON response to extract the character's name
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  }
});
