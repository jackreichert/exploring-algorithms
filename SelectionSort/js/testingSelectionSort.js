'use strict';

Array.prototype.equals = function(array) {
	// if the other array is a falsy value, return
	if (!array) {
		return false;
	}

	// compare lengths - can save a lot of time
	if (this.length != array.length) {
		return false;
	}

	for (var i = 0, l = this.length; i < l; i++) {
		// Check if we have nested arrays
		if (this[i] instanceof Array && array[i] instanceof Array) {
			// recurse into the nested arrays
			if (!this[i].equals(array[i])) {
				return false;
			}
		}
		else if (this[i] != array[i]) {
			// Warning - two different object instances will never be equal: {x:20} != {x:20}
			return false;
		}
	}
	return true;
};
Object.defineProperty(Array.prototype, 'equals', {enumerable: false});

function generateHugeList(length) {
	var longList = [];
	for (var i = 0; i < length; i++) {
		longList.push(Math.round(Math.random() * length));
	}
	return longList;
}

function isArrayInOrder(arrayToCheck) {
	for (var i = 0; i < arrayToCheck.length - 1; i++) {
		if (arrayToCheck[i] > arrayToCheck[i + 1]) {
			return false;
		}
	}
	return true;
}

QUnit.module('test SelectionSort', {
	beforeEach: function() {
		this.selectionSort = new SelectionSort();
	},
});

const test_0 = 'Can create SelectionSort object';
QUnit.test(test_0, function(assert) {
	assert.ok('SelectionSort' === this.selectionSort.constructor.name,
		`${test_0}`);
});

const test_1 = 'When given list of unique positive numbers, can find lowest number';
QUnit.test(test_1, function(assert) {
	const numberList = [23, 2, 43, 54, 5, 12, 4, 76, 1, 544, 4];
	assert.ok(8 === this.selectionSort.findIndexOfLowest(numberList), test_1);
});

const test_2 = 'When given list of unique numbers, can find lowest number';
QUnit.test(test_2, function(assert) {
	const numberList = [23, 2, 43, -52, 5, 12, 4, 76, 1, 544, -1, 4];
	assert.ok(3 === this.selectionSort.findIndexOfLowest(numberList), test_2);
});

const test_3 = 'When given list of numbers, can find lowest number';
QUnit.test(test_3, function(assert) {
	const numberList = [23, 2, 43, -54, 5, 12, 5, 4, 76, 1, 544, -1, 4, -54];
	assert.ok(3 === this.selectionSort.findIndexOfLowest(numberList), test_3);
});

const test_4 = 'Swapping numbers in small list, where from > to';
QUnit.test(test_4, function(assert) {
	const numberList = [23, 2, 43, -54, 5, 12, 5, 4, 76, 1, 544, -1, 4, -54];
	assert.ok([23, 2, 43, 544, 5, 12, 5, 4, 76, 1, -54, -1, 4, -54].equals(
		this.selectionSort.swapFromTo(numberList, 10, 3)), test_4);
});

const test_5 = 'Swapping numbers in small list, where from < to';
QUnit.test(test_5, function(assert) {
	const numberList = [23, 2, 43, -54, 5, 12, 5, 4, 76, 1, 544, -1, 4, -54];
	assert.ok([23, 2, 43, -54, 1, 12, 5, 4, 76, 5, 544, -1, 4, -54].equals(
		this.selectionSort.swapFromTo(numberList, 4, 9)), test_5);
});

const test_6 = 'Can sort small list';
QUnit.test(test_6, function(assert) {
	const numberList = [23, 2, 43, -54, 5, 12, 5, 4, 76, 1, 544, -1, 4, -54];
	assert.ok(isArrayInOrder(this.selectionSort.sort(numberList)), test_6);
});

const test_7 = 'Can sort large list';
QUnit.test(test_7, function(assert) {
	const numberList = generateHugeList(5000);
	assert.ok(isArrayInOrder(this.selectionSort.sort(numberList)), test_7);
});
