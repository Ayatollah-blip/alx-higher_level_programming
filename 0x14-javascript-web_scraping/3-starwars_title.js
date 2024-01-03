#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const filePath = 'https://swapi-api.alx-tools.com/api/films/';
if (!filePath) {
  process.exit(1);
}

request.get(filePath + id, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode !== 200) {
    console.log('Error:', response.statusCode);
  } else {
    const film = JSON.parse(body);
    console.log(film.title);
  }
});
