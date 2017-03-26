'use strict';

Array.prototype.equals = function (array) {
    // if the other array is a falsy value, return
    if (!array)
        return false;

    // compare lengths - can save a lot of time
    if (this.length != array.length)
        return false;

    for (var i = 0, l=this.length; i < l; i++) {
        // Check if we have nested arrays
        if (this[i] instanceof Array && array[i] instanceof Array) {
            // recurse into the nested arrays
            if (!this[i].equals(array[i]))
                return false;
        }
        else if (this[i] != array[i]) {
            // Warning - two different object instances will never be equal: {x:20} != {x:20}
            return false;
        }
    }
    return true;
}

function generateHugeList(length) {
  var longList = [];
  for( var i=0;i < length; i++) {
    longList.push(Math.round(Math.random()*length));
  }
  return longList;
}

function isArrayInOrder(arrayToCheck) {
  for(var i; i < arrayToCheck.length-1; i++) {
    if (arrayToCheck[i] > arrayToCheck[1+1]) {
      return false;
    }
  }
  return true;
}

QUnit.module("test MergeSort", {
  beforeEach : function() {
    this.mergeSort = new MergeSort();
  }
});

QUnit.test( "Can create MergeSort object", function( assert ) {
  assert.ok( 'MergeSort' === this.mergeSort.constructor.name, "Passed!" );
});

QUnit.test( "When [1] is given, sort returns [1]", function (assert) {
  assert.ok( [1].equals(this.mergeSort.sort([1])));
});

QUnit.test( "When [2,1] is given, sort returns [1,2]", function (assert) {
  assert.ok( [1,2].equals(this.mergeSort.sort([2,1])));
});

QUnit.test( "When [1,2] is given, sort returns [1,2]", function (assert) {
  assert.ok( [1,2].equals(this.mergeSort.sort([1,2])));
});

QUnit.test( "When [1,2,3] is given, sort returns [1,2,3]", function (assert) {
  assert.ok( [1,2,3].equals(this.mergeSort.sort([1,2,3])));
});

QUnit.test( "When [3,2,1] is given, sort returns [1,2,3]", function (assert) {
  assert.ok( [1,2,3].equals(this.mergeSort.sort([3,2,1])));
});

QUnit.test( "When [2,3,1] is given, sort returns [1,2,3]", function (assert) {
  assert.ok( [1,2,3].equals(this.mergeSort.sort([2,3,1])));
});

QUnit.test( "When [1,3,2] is given, sort returns [1,2,3]", function (assert) {
  assert.ok( [1,2,3].equals(this.mergeSort.sort([1,3,2])));
});

QUnit.test( "When [3,2,2,1] is given, sort returns [1,2,2,3]", function (assert) {
  assert.ok( isArrayInOrder(this.mergeSort.sort([3,2,2,1])));
});

QUnit.test("Can sort large list", function( assert ) {
  const numberList = generateHugeList(5000);
  assert.ok(isArrayInOrder(this.mergeSort.sort(numberList)), "Passed!")
});
