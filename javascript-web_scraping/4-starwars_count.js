#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const characterId = 18;
const characterurl = `https://swapi-api.hbtn.io/api/films/${characterId}/`;

request(url, (error, response, body) => {
  if (error) { return console.error(error); }

  const data = JSON.parse(body);
  const count = data.results
    .filter(movie => movie.characters.includes(characterurl))
    .length;

  console.log(count);
});
