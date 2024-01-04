#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('0');
} else if (process.argv.length === 3) {
  console.log('0');
} else {
  let i;
  const arr = [];
  for (i = 2; i < process.argv.length; i++) {
    arr.push(parseInt(process.argv[i]));
  }
  let n;
  let num = arr[0];
  for (i = 1; i < arr.length; i++) {
    if (arr[i] > num) {
      num = arr[i];
    }
  }
  for (i = 0; i < arr.length; i++) {
    if (arr[i] === num) {
      continue;
    } else {
      n = arr[i];
      break;
    }
  }
  for (i = 0; i < arr.length; i++) {
    if (arr[i] === num) {
      continue;
    } else {
      if (arr[i] > n) {
        n = arr[i];
      }
    }
  }
  console.log(n);
}
