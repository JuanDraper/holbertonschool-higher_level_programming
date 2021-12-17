#!/usr/bin/node
/* occurrences
*/
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (const j of list) {
    if (j === searchElement) {
      i++;
    }
  }
  return (i);
};
