#!/usr/bin/node
/* advanced
*/
const arr = require('./100-data.js').list;
console.log(arr);
console.log(arr.map(function (x, i) { return (x * i); }));
