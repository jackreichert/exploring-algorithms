'use strict';

QUnit.test("New insertion search init", function (assert) {
  var insertionSort = new InsertionSort();
  assert.ok(undefined !== insertionSort, 'Passed!');
});

QUnit.test("When 1 is given, insertIntoPlace returns 1", function (assert) {
  var insertionSort = new InsertionSort();
  assert.ok('1' === insertionSort.insertIntoPlace([], 1).toString());
});
