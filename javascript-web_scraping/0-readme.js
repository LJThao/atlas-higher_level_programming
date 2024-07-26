#!/usr/bin/node

// Loads the file system module for interaction
const fs = require('fs');

// Reading the file content
fs.readFile(process.argv[2], 'utf8', (err, data) => {
    // Checking for error
    if (err) {
        return console.error(`Error: ${err.message}`);
    }
    // Printing the file content
    console.log(data);
});