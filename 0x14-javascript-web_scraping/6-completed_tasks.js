#!/usr/bin/node

// Import the 'request' module to make HTTP request
const request = require('request');

// Get the API URL from command-line argumets
const apiUrl = process.argv[2];

// Make a GET request to the specified API URL
request(apiUrl, (error, response, body) => {
  // If an error occurs during the request, print the error
  if (error) {
    console.error(error);
  } else {
    // Parse the JSON response to extract the task data
    const taskData = JSON.parse(body);

    // Create an object to store the count of completed tasks for each user
    const completedTasksCount = {};

    // Loop throught the taskd and count completed tasks by user ID
    taskData.forEach((task) => {
      if (task.completed) {
        const userId = task.userId;
        if (completedTasksCount[userId]) {
          completedTasksCount[userId]++;
        } else {
          completedTasksCount[userId] = 1;
        }
      }
    });

    // Print the count of completed tasks for each user as an object
    console.log(completedTasksCount);
  }
});
