#!/usr/bin/node

const process = require('process');
const request = require('request');

const argv = process.argv;

const URL = 'https://swapi-api.alx-tools.com/api/films/';
const moviePosition = argv[2];

function fetchData (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

async function displayData () {
  try {
    const movieResponse = await new Promise((resolve, reject) => {
      request(URL, (error, response, body) => {
        if (error) {
          reject(new Error(`Error fetching films data: ${error}`));
        } else {
          resolve(body);
        }
      });
    });

    const responseData = JSON.parse(movieResponse);
    const movie = responseData.results[moviePosition - 1];

    if (!movie) {
      console.error('Movie not found.');
      return;
    }

    const movieCharacters = movie.characters;

    for (const character of movieCharacters) {
      try {
        const characterData = await fetchData(character);
        const characterDataJson = JSON.parse(characterData);
        console.log(characterDataJson.name);
      } catch (error) {
        console.error(`Error fetching data for ${character}: ${error}`);
      }
    }
  } catch (error) {
    console.error(error);
  }
}

displayData();
