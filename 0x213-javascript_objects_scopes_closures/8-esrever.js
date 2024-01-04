#!/usr/bin/node
exports.esrever = function (list) {
  let i;
  let b = list.length - 1;
  for (i = 0; i <= b; i++) {
    const tmp = list[b];
    list[b] = list[i];
    list[i] = tmp;
    b--;
  }
  return (list);
};
