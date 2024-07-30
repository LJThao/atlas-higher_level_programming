#!/usr/bin/node

const request = require('request');

const url = process.argv[2] || 'https://swapi-api.hbtn.io/api/films/';
const characterId = '/18/';

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  try {
    const films = JSON.parse(body).results;
    const count = films.reduce((acc, film) =>
      acc + film.characters.some(url => url.includes(characterId)), 0);

    console.log(count);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
