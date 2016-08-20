'use strict';

QUnit.test("New insertion search init", function (assert) {
  var insertionSort = new InsertionSort();
  assert.ok(undefined !== insertionSort, 'Passed!');
});

QUnit.test("When 1 is given, getPositionForNewVal returns 0", function (assert) {
  var insertionSort = new InsertionSort();
  assert.ok(0 === insertionSort.getPositionForNewVal(1, []));
});

QUnit.test("When 2 is given to 3,4, getPositionForNewVal returns 0", function (assert) {
  var insertionSort = new InsertionSort();
  assert.ok(0 === insertionSort.getPositionForNewVal(2, [3,4]));
});

QUnit.test("When 3 is given to 2,7,4, getPositionForNewVal returns 1", function (assert) {
  var insertionSort = new InsertionSort();
  assert.ok(1 === insertionSort.getPositionForNewVal(3, [2,7,4]));
});

QUnit.test("When 3,2,5,4,7,4 is given, sort returns 2,3,4,4,5,7", function (assert) {
  var insertionSort = new InsertionSort();
  assert.ok('2,3,4,4,5,7' === insertionSort.sort([3,2,5,4,7,4]).toString());
});
