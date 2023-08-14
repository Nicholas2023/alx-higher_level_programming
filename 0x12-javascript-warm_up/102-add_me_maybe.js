#!/usr/bin/node

// Define the addMeMaybe function
function addMeMaybe (number, theFunction) {
  number++;
  theFunction(number);
}

//Export the function
module.exports = {
  addMeMaybe
};
