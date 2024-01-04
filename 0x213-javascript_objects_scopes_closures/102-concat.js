#!/usr/bin/node
const process = require('process');
const fs = require('fs');
if (process.argv.length === 5) {
  const data1 = fs.readFileSync(process.argv[2]);
  const msg1 = data1.toString();
  const data2 = fs.readFileSync(process.argv[3]);
  const msg2 = data2.toString();
  fs.appendFile(process.argv[4], msg1, function (err) {
    if (err) throw err;
  });
  fs.appendFile(process.argv[4], msg2, function (err) {
    if (err) throw err;
  });
}
