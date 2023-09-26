#!/usr/bin/node

// Import the 'request' module to make HTTp requests
const request = require('request');

// Get the Movie ID from command-line arguments
const movieId = process.argv[2];

// Define the URL to the Star Wars API for the movie with the given ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the specified URL
request(url, (error, response, body) => {
  if (error) {
    // If an error occurs during request, print the error
    console.error(error);
  } else {
    // Parse the JSON response to extract the character data
    const movieData = JSON.parse(body);

    // Print the name of all character in the movie, one character per line
    movieData.characters.forEach((characterUrl) => {
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
