#!/usr/bin/node
const num = parseInt(process.argv[2]);
let i;
let j;
let msg = '';
if (isNaN(num) === true) {
  console.log('Missing size');
} else if (num > 0) {
  for (i = 0; i < num; i++) {
    for (j = 0; j < num; j++) {
      msg = msg + 'X';
    }
    if (i !== num - 1) {
      msg = msg + '\n';
    }
  }
  console.log(msg);
}
