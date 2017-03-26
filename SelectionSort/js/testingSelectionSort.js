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

QUnit.module("test SelectionSort", {
  beforeEach : function() {
    this.selectionSort = new SelectionSort();
  }
});

QUnit.test( "Can create SelectionSort object", function( assert ) {
  assert.ok( 'SelectionSort' === this.selectionSort.constructor.name, "Passed!" );
});

QUnit.test("When given list of unique positive numbers, can find lowest number", function( assert ) {
  const numberList = [23,2,43,54,5,12,4,76,1,544,4];
  assert.ok(8 === this.selectionSort.findIndexOfLowest(numberList), "Passed!")
});

QUnit.test("When given list of unique numbers, can find lowest number", function( assert ) {
  const numberList = [23,2,43,-52,5,12,4,76,1,544,-1,4];
  assert.ok(3 === this.selectionSort.findIndexOfLowest(numberList), "Passed!")
});

QUnit.test("When given list of numbers, can find lowest number", function( assert ) {
  const numberList = [23,2,43,-54,5,12,5,4,76,1,544,-1,4,-54];
  assert.ok(3 === this.selectionSort.findIndexOfLowest(numberList), "Passed!")
});

QUnit.test("Swapping numbers in small list, where from > to", function( assert ) {
  const numberList = [23,2,43,-54,5,12,5,4,76,1,544,-1,4,-54];
  assert.ok([23,2,43,544,5,12,5,4,76,1,-54,-1,4,-54].equals(this.selectionSort.swap(numberList, 10, 3)), "Passed!")
});

QUnit.test("Swapping numbers in small list, where from < to", function( assert ) {
  const numberList = [23,2,43,-54,5,12,5,4,76,1,544,-1,4,-54];
  assert.ok([23,2,43,544,5,12,5,4,76,1,-54,-1,4,-54].equals(this.selectionSort.swap(numberList, 3, 10)), "Passed!")
});

QUnit.test("Can sort small list", function( assert ) {
  const numberList = [23,2,43,-54,5,12,5,4,76,1,544,-1,4,-54];
  assert.ok(isArrayInOrder(this.selectionSort.sort(numberList)), "Passed!")
});

QUnit.test("Can sort large list", function( assert ) {
  const numberList = generateHugeList(5000);
  assert.ok(isArrayInOrder(this.selectionSort.sort(numberList)), "Passed!")
});
