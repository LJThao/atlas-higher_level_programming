#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const todos = JSON.parse(body);
  const tasks = todos.reduce((acc, { userId, completed }) => {
    if (completed) acc[userId] = (acc[userId] || 0) + 1;
    return acc;
  }, {});

  console.log(tasks);
});
