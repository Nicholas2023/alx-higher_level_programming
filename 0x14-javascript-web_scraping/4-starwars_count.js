#!/usr/bin/node

// Import the 'request' module to make HTTP request
const request = require('request');

// Get the API URL from the command-line arguments
const apiUrl = process.argv[2];

// Character ID for Wedge Antilles
const characterId = 18;

// Make a GET request to the Star Wars API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    // If an error occurs during the request, print the error
    console.error(error);
  } else {
    // Parse the JSON response to extract the films data
    const filmsData = JSON.parse(body).results;

    // Filter the films where Wedge Antilles is present (character ID 18)
    const count = filmsData.filter((film) =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    ).length;

    // Print the number of films where Wedge Antilles is present
    console.log(count);
  }
});
