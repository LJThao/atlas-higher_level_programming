#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const characterId = 18;
const characterurl = `https://swapi-api.hbtn.io/api/people/${characterId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Request Error:', error);
    return;
  }

  try {
    const data = JSON.parse(body);

    console.log('API Response:', data);

    if (!data.results || !Array.isArray(data.results)) {
      console.error('Error: Unexpected data structure.');
      process.exit(1);
    }

    const count = data.results
      .filter(movie => movie.characters && movie.characters.includes(characterurl))
      .length;

    console.log(count);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
