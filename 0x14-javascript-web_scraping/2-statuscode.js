#!/usr/bin/node

const request = require('request');

const filePath = process.argv;

if (!filePath) {
  process.exit(1);
}

request(filePath[2], function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    console.log('code: ', response.statusCode);
  }
});
