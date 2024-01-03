#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv;

if (!filePath) {
  process.exit(1);
}

fs.writeFile(filePath[2], filePath[3], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
});
