'use strict';

QUnit.module("test linked list", {
  beforeEach : function() {
    this.linkedList = new LinkedList();
  }
});

QUnit.test("New linked list init", function (assert) {
  assert.ok(undefined !== this.linkedList, 'Passed!');
});

QUnit.test("New linked list, next is null", function (assert) {
  assert.ok(null === this.linkedList.getNext(), 'Passed!');
});

QUnit.test("New Linked list, getLength is 0", function (assert) {
  assert.ok(0 === this.linkedList.getLength(), 'Passed!');
});

QUnit.test("Add value once to list, getLength is 1", function (assert) {
  this.linkedList.add(5);
  assert.ok(1 === this.linkedList.getLength(), 'Passed!');
});

QUnit.test("Add value once, searchValueAt(0) returns value", function (assert) {
  this.linkedList.add(5);
  assert.ok(5 === this.linkedList.searchValueAt(0), 'Passed!');
});

QUnit.test("Add value once, searchValueAt(1) returns null", function (assert) {
  this.linkedList.add(5);
  assert.ok(null === this.linkedList.searchValueAt(1), 'Passed!');
});

QUnit.test("Add two values, getLength is 2", function (assert) {
  this.linkedList.add(5);
  this.linkedList.add(8);
  assert.ok(2 === this.linkedList.getLength(), 'Passed!');
});

QUnit.test("Add two values, searchValueAt(1) returns second value", function (assert) {
  this.linkedList.add(5);
  this.linkedList.add(8);
  assert.ok(8 === this.linkedList.searchValueAt(1), 'Passed!');
});

QUnit.test("Add two values, searchValueAt(0) returns first value", function (assert) {
  this.linkedList.add(5);
  this.linkedList.add(8);
  assert.ok(5 === this.linkedList.searchValueAt(0), 'Passed!');
});

QUnit.test("Remove node on empty list, length is 0", function (assert) {
  this.linkedList.removeNodeAt(0);
  assert.ok(0 === this.linkedList.getLength(), 'Passed!');
});

QUnit.test("Add value, remove node, length is 0", function (assert) {
  this.linkedList.add(5);
  this.linkedList.removeNodeAt(0);
  assert.ok(0 === this.linkedList.getLength(), 'Passed!');
});

QUnit.test("Add value, remove node, list is empty", function (assert) {
  this.linkedList.add(5);
  this.linkedList.removeNodeAt(0);
  assert.ok(null === this.linkedList.searchValueAt(0), 'Passed!');
});

QUnit.test("Add value, remove node, add value, first is second value", function (assert) {
  this.linkedList.add(5);
  this.linkedList.removeNodeAt(0);
  this.linkedList.add(8);
  assert.ok(8 === this.linkedList.searchValueAt(0), 'Passed!');
});

QUnit.test("Add two values, remove second, length is 1", function (assert) {
  this.linkedList.add(5);
  this.linkedList.add(8);
  this.linkedList.removeNodeAt(1);
  assert.ok(1 === this.linkedList.getLength(), 'Passed!');
});

QUnit.test("Add two values, remove at third position, length is 2", function (assert) {
  this.linkedList.add(5);
  this.linkedList.add(8);
  this.linkedList.removeNodeAt(2);
  assert.ok(2 === this.linkedList.getLength(), 'Passed!');
});

QUnit.test("Add two values, remove second, first is value and next is empty", function (assert) {
  this.linkedList.add(5);
  this.linkedList.add(8);
  this.linkedList.removeNodeAt(1);
  assert.ok(5 === this.linkedList.searchValueAt(0), 'Passed!');
  assert.ok(null === this.linkedList.getNext(), 'Passed!');
});

QUnit.test("Add two values, remove first, length is 1", function (assert) {
  this.linkedList.add(5);
  this.linkedList.add(8);
  this.linkedList.removeNodeAt(0);
  assert.ok(1 === this.linkedList.getLength(), 'Passed!');
});

QUnit.test("Add two values, remove first, first is second value", function (assert) {
  this.linkedList.add(5);
  this.linkedList.add(8);
  this.linkedList.removeNodeAt(0);
  assert.ok(8 === this.linkedList.searchValueAt(0), 'Passed!');
});

QUnit.test("Add three values, remove second, length is 2", function (assert) {
  this.linkedList.add(5);
  this.linkedList.add(8);
  this.linkedList.add(7);
  this.linkedList.removeNodeAt(1);
  assert.ok(2 === this.linkedList.getLength(), 'Passed!');
});

QUnit.test("Add three values, remove second, first is value and second is third value", function (assert) {
  this.linkedList.add(5);
  this.linkedList.add(8);
  this.linkedList.add(7);
  this.linkedList.removeNodeAt(1);
  assert.ok(5 === this.linkedList.searchValueAt(0), 'Passed!');
  assert.ok(7 === this.linkedList.searchValueAt(1), 'Passed!');
});
