#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    let j;
    let msg = '';
    if (this.width > 0 && this.height > 0) {
      for (i = 0; i < this.height; i++) {
        for (j = 0; j < this.width; j++) {
          msg = msg + 'X';
        }
        if (i !== this.height - 1) {
          msg = msg + '\n';
        }
      }
      console.log(msg);
    }
  }
}
module.exports = Rectangle;
