#!/usr/bin/node

const request = require('request');

// Recursive function to fetch and print character names sequentially
const fetchCharacterNames = (characters, index) => {
  if (index >= characters.length) return; // Base case: all characters fetched

  request(characters[index], (err, response, body) => {
    if (err) {
      console.error('Error fetching character:', err);
    } else {
      console.log(JSON.parse(body).name); // Print character name
      fetchCharacterNames(characters, index + 1); // Recursive call to the next character
    }
  });
};

// Fetch the movie details
request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, response, body) => {
  if (err) {
    console.error('Error fetching movie details:', err);
  } else {
    const characters = JSON.parse(body).characters; // Get the list of character URLs
    fetchCharacterNames(characters, 0); // Start fetching character names
  }
});
