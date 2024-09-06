#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];
const filmEndPoint = `https://swapi-api.hbtn.io/api/films/${movieId}`;

// Function to fetch characters from the movie
const fetchCharacters = async () => {
  return new Promise((resolve, reject) => {
    request(filmEndPoint, (err, res, body) => {
      if (err) {
        reject(`Error: ${err}`);
      } else if (res.statusCode !== 200) {
        reject(`Error: ${res.statusCode}`);
      } else {
        // Parse response body and get characters list
        const characters = JSON.parse(body).characters;
        resolve(characters);
      }
    });
  });
};

// Function to fetch and print character names
const printCharacterNames = async (characters) => {
  for (const characterUrl of characters) {
    await new Promise((resolve, reject) => {
      request(characterUrl, (err, res, body) => {
        if (err) {
          reject(`Error: ${err}`);
        } else if (res.statusCode !== 200) {
          reject(`Error: ${res.statusCode}`);
        } else {
          // Parse response body and print character name
          const name = JSON.parse(body).name;
          console.log(name);
          resolve();
        }
      });
    });
  }
};

// Main function to coordinate fetching and printing
const main = async () => {
  try {
    const characters = await fetchCharacters();
    await printCharacterNames(characters);
  } catch (error) {
    console.error(error);
  }
};

main();

