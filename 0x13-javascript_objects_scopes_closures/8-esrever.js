#!/usr/bin/node
/* working on lists
*/
exports.esrever = function (list) {
  let l = list.length - 1;
  const newList = [];
  while (l >= 0) {
    newList.push(list[l]);
    l--;
  }
  return (newList);
};
