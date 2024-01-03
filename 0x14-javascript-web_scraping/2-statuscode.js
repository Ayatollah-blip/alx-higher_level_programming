#!/usr/bin/node

const request = require('request');

const filePath = process.argv[2];

if (!filePath) {
  process.exit(1);
}

request.get(filePath, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    console.log('code:', response.statusCode);
  }
});
