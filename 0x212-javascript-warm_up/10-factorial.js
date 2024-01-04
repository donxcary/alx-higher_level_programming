#!/usr/bin/node
function factorial (num) {
  if (num === 0 || isNaN(num) === true) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}
const n = parseInt(process.argv[2]);
const fact = factorial(n);
console.log(fact);
