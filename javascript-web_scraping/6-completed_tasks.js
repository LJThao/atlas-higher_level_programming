#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const userId = parseInt(process.argv[3], 10);

request(url, (error, _, body) => {
  if (error) return console.error(error);

  const todos = JSON.parse(body);
  const tasks = {};

  todos.forEach(task => {
    if (task.completed) {
      tasks[task.userId] = (tasks[task.userId] || 0) + 1;
    }
  });

  if (userId) {
    console.log(`${userId}: ${tasks[userId] || 0}`);
  } else {
    for (const [id, count] of Object.entries(tasks)) {
      console.log(`${id}: ${count}`);
    }
  }
});
