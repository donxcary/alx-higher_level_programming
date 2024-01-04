#!/usr/bin/node
const Square1 = require('./5-square');
class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let i;
      let j;
      let msg = '';
      if (this.width > 0 && this.height > 0) {
        for (i = 0; i < this.height; i++) {
          for (j = 0; j < this.width; j++) {
            msg = msg + c;
          }
          if (i !== this.height - 1) {
            msg = msg + '\n';
          }
        }
        console.log(msg);
      }
    }
  }
}
module.exports = Square;
