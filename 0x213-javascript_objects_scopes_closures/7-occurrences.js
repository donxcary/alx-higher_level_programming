#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i;
  let b = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      b = b + 1;
    }
  }
  return (b);
};
