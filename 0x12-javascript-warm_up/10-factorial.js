#!/usr/bin/node
/* uwu factorio
*/
const num = parseInt(process.argv[2]);
function factorial (i) {
  if (!i) {
    return (1);
  } else {
    return (i * factorial(i - 1));
  }
}
console.log(factorial(num));
