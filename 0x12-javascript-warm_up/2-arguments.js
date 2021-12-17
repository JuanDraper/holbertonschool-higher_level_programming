#!/usr/bin/node
/*
passing arguments
*/
const qargs = process.argv.length;
if (qargs === 2) {
  console.log('No argument');
} else if (qargs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
