'use strict';

QUnit.module("test insertion sort", {
  beforeEach : function() {
    this.insertionSort = new InsertionSort();
  }
});

QUnit.test("New insertion search init", function (assert) {
  assert.ok(undefined !== this.insertionSort, 'Passed!');
});

QUnit.test("When 1 is given, getPositionForNewVal returns 0", function (assert) {
  assert.ok(0 === this.insertionSort.getPositionForNewVal(1, []));
});

QUnit.test("When 2 is given to [3,4], getPositionForNewVal returns 0", function (assert) {
  assert.ok(0 === this.insertionSort.getPositionForNewVal(2, [3,4]));
});

QUnit.test("When 3 is given to [2,7,4], getPositionForNewVal returns 1", function (assert) {
  assert.ok(1 === this.insertionSort.getPositionForNewVal(3, [2,7,4]));
});

QUnit.test("When [3,2,5,4,7,4] is given, sort returns [2,3,4,4,5,7]", function (assert) {
  assert.ok('2,3,4,4,5,7' === this.insertionSort.sort([3,2,5,4,7,4]).toString());
});

QUnit.test("When [8682,2602,5961,4659,432,8230,111,3921,2841,5913,4876,800,6748,5720,4660,327,2305,3571,9919,8277,6168,2305,3359,9292,7043] is given, sort returns [111,327,432,800,2305,2305,2602,2841,3359,3571,3921,4659,4660,4876,5720,5913,5961,6168,6748,7043,8230,8277,8682,9292,9919]", function (assert) {
  assert.ok('111,327,432,800,2305,2305,2602,2841,3359,3571,3921,4659,4660,4876,5720,5913,5961,6168,6748,7043,8230,8277,8682,9292,9919' === this.insertionSort.sort([8682,2602,5961,4659,432,8230,111,3921,2841,5913,4876,800,6748,5720,4660,327,2305,3571,9919,8277,6168,2305,3359,9292,7043]).toString());
});
