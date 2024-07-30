#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (err, response) => {
  if (err) {
    console.error;
    return;
  }
  if (response) {
    console.log(`code: ${response.statusCode}`);
  }
});