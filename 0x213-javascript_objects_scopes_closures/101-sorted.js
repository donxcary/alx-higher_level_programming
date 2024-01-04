#!/usr/bin/node
const dict = require('./101-data').dict;
const vals = Object.values(dict);
const myArr = [vals[[0]]];
let i;
let j;
for (i = 0; i < vals.length; i++) {
  if (myArr.includes(vals[i]) === true) {
    continue;
  }
  myArr.push(vals[i]);
}
const keys = Object.keys(dict);
const newDict = {};
if (vals.length !== 0) {
  for (j = 0; j < myArr.length; j++) {
    newDict[myArr[j]] = [];
  }
  for (i = 0; i < vals.length; i++) {
    for (j = 0; j < myArr.length; j++) {
      if (dict[keys[i]] === myArr[j]) {
        newDict[myArr[j]].push(keys[i]);
      }
    }
  }
}
console.log(newDict);
