#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  // Function to handle fetching each character
  function fetchCharacter (index) {
    if (index === characters.length) return;

    request(characters[index], (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);

      fetchCharacter(index + 1);
    });
  }

  fetchCharacter(0);
});
