'use strict';

QUnit.test("New insertion search init", function (assert) {
  var insertionSort = new InsertionSort();
  assert.ok(undefined !== insertionSort, 'Passed!');
});

QUnit.test("When one is given, one is returned", function (assert) {
  var insertionSort = new InsertionSort();
  assert.ok( '1' === insertionSort.sort([1]).toString(), 'Passed!');
});

QUnit.test("When 1,2 is given, 1,2 is returned", function (assert) {
  var insertionSort = new InsertionSort();
  assert.ok( '1,2' === insertionSort.sort([1,2]).toString(), 'Passed!');
});

QUnit.test("When 2,1 is given, 1,2 is returned", function (assert) {
  var insertionSort = new InsertionSort();
  assert.ok( '1,2' === insertionSort.sort([2,1]).toString(), 'Passed!');
});

QUnit.test("When 1,2,3 is given, 1,2,3 is returned", function (assert) {
  var insertionSort = new InsertionSort();
  assert.ok( '1,2,3' === insertionSort.sort([1,2,3]).toString(), 'Passed!');
});

QUnit.test("When 3,1,2 is given, 1,2,3 is returned", function (assert) {
  var insertionSort = new InsertionSort();
  assert.ok( '1,2,3' === insertionSort.sort([3,1,2]).toString(), 'Passed!');
});

QUnit.test("When 3,9,32,34543,3,3,23,1,2,4 is given, 1,2,3,3,3,4,9,32,34543 is returned", function (assert) {
  var insertionSort = new InsertionSort();
  assert.ok( '1,2,3,3,3,4,9,23,32,34543' === insertionSort.sort([3,9,32,34543,3,3,23,1,2,4]).toString(), 'Passed!');
});
