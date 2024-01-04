#!/usr/bin/node
const list = require('./100-data').list;
let i = -1;
function num () {
  i = i + 1;
  return (i);
}
console.log(list);
const map1 = list.map(x => x * (num()));
console.log(map1);
