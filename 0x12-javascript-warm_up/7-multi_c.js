#!/usr/bin/node
/* args and loops
*/
const num = parseInt(process.argv[2]);
let i = 0;
if (!num) {
  console.log('Missing number of occurrences');
} else {
  for (i; i < num; i++) {
    console.log('C is fun');
  }
}
