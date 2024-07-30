#!/usr/bin/node

const request = require('request');

const episodeId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${episodeId}/`;

request(url, (err, response, body) => {
    if (err) return console.error(err);
    try {
        const data = JSON.parse(body);
        console.log(data.title || '');
    } catch (e) {
        console.error(e);
    }
});
