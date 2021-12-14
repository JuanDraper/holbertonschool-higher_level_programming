#!/usr/bin/node
/* more squareing
*/
const sqr = require('./5-square');
let char = 'X';
module.exports = class square extends sqr {
  charPrint (c) {
    if (c) {
      char = c;
    }
    console.log((char.repeat(this.width) + '\n').repeat(this.height - 1) + char.repeat(this.width));
  }
};
