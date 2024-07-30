#!/usr/bin/node

// Loads the file system module for interaction
const fs = require('fs');

// Extracting the file path and content from process.argv
const [filePath, content] = process.argv.slice(2);

// Writing the the content to the file using utf-8 encoding
fs.writeFile(filePath, content, 'utf8', (err) => {
  // If an error occur then this happens
  if (err) {
    console.error(err);
  }
});
