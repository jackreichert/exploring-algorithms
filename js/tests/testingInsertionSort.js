'use strict';

QUnit.test("New insertion search init", function (assert) {
  var insertionSort = new InsertionSort();
  assert.ok(undefined !== insertionSort, 'Passed!');
});

QUnit.test("When 1 is given, insertIntoPlace returns 1", function (assert) {
  var insertionSort = new InsertionSort();
  assert.ok('1' === insertionSort.insertIntoPlace(1, []).toString());
});

QUnit.test("When 2 is given to 3,4, insertIntoPlace returns 2,3,4", function (assert) {
  var insertionSort = new InsertionSort();
  console.log(insertionSort.insertIntoPlace(2, [3,4]).toString());
  assert.ok('2,3,4' === insertionSort.insertIntoPlace(2, [3,4]).toString());
});

QUnit.test("When 3 is given to 2,7,4, insertIntoPlace returns 2,3,7,4", function (assert) {
  var insertionSort = new InsertionSort();
  assert.ok('2,3,7,4' === insertionSort.insertIntoPlace(3, [2,7,4]).toString());
});

QUnit.test("When 3,2,5,4,7,4 is given, sort returns 2,3,4,4,5,7", function (assert) {
  var insertionSort = new InsertionSort();
  assert.ok('2,3,4,4,5,7' === insertionSort.sort([3,2,5,4,7,4]).toString());
});
