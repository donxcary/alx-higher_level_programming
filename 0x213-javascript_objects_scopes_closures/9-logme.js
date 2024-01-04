#!/usr/bin/node
let callCount = -1;
exports.logMe = function (item) {
  callCount += 1;
  console.log(callCount + ': ' + item);
};
