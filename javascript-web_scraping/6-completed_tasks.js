#!/bin/usr/node

const request = require('request');

const url = process.argv[2];

request(url, (error, _, body) => {
  if (error) return console.error(error);

  const todos = JSON.parse(body);
  const tasks = {};

  todos.forEach(task => {
    if (task.completed) {
      tasks[task.userId] = (tasks[task.userId] || 0) + 1;
    }
  });

  for (const userId in tasks) {
    console.log(`${userId}: ${tasks[userId]}`);
  }
});
