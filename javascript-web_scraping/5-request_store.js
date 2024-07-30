#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const [url, filePath] = process.argv.slice(2);

request(url, (error, _, body) => {
    if (error) return console.error(error);
    fs.writeFile(filePath, body, 'utf8', (err) => {
        if (err) console.error(err);
    });
});
