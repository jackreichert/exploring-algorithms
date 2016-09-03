'use strict';

QUnit.module("test Stack", {
  beforeEach : function() {
    this.stack = new Stack();
  }
});

QUnit.test( "Can create Stack object", function( assert ) {
  assert.ok( 'Stack' === this.stack.constructor.name, "Passed!" );
});

QUnit.test( "Newly created stacks should be empty", function ( assert ) {
  assert.ok( 0 === this.stack.getSize(), "Passed!");
  assert.ok( this.stack.isEmpty(), "Passed!" );
});

QUnit.test( "After one push, stack size should be one", function ( assert ) {
  this.stack.push(1);
  assert.ok( 1 === this.stack.getSize(), "Passed!");
  assert.ok( !this.stack.isEmpty(), "Passed!" );
})

QUnit.test( "After one push and one pop, should be empty", function(assert) {
  this.stack.push(1);
  this.stack.pop();
  assert.ok( this.stack.isEmpty(), "Passed!" );
});

// QUnit.test( "When pushed passed limit, stack overflows");

QUnit.test( "When popped passed limit, stack underflows", function (assert) {
  assert.throws(
    function() {
      this.stack.push(1);
      this.stack.pop();
      this.stack.pop();
    }, new Error("StackUnderflow"), "Passed!" );
});

QUnit.test( "When two values are pushed then one is popped, size is one", function(assert) {
  this.stack.push(1);
  this.stack.push(2);
  this.stack.pop();
  assert.ok( 1 === this.stack.getSize(), "Passed!" );
});

QUnit.test( "When one is pushed one is popped", function (assert) {
  this.stack.push(1);
  assert.ok( 1 === this.stack.pop(), "Passed!" );
});

QUnit.test( "When one and two are pushed two and one are popped", function (assert) {
  this.stack.push(1);
  this.stack.push(2);
  assert.ok( 2 === this.stack.pop(), "Passed!" );
  assert.ok( 1 === this.stack.pop(), "Passed!" );
});

// QUnit.test("When creating stack with negative size, should through IllegalCapacity");

// QUnit.test("When Creating stack with zero capacity, any push should overflow");

QUnit.test( "When one is pushed, one is on top", function (assert) {
  this.stack.push(1);
  assert.ok( 1 === this.stack.top(), "Passed!");
  assert.ok( 1 === this.stack.getSize(), "Passed!");
});

QUnit.test("When stack is empty, top throws empty", function (assert) {
  assert.throws(function () {
    this.stack.top();
  }, new Error("Empty"), 'Passed!');
});

// QUnit.test("With zero capacity stack, top throws empty");

QUnit.test("Given stack with one two pushed, find one and two", function (assert) {
    this.stack.push(1);
    this.stack.push(2);
    assert.ok( 1 == this.stack.find(1), "Passed!" );
    assert.ok( 0 == this.stack.find(2), "Passed!" );
});

QUnit.test("Given a stack with no two, find two returns null", function (assert) {
    assert.ok(null == this.stack.find(2), "Passed!");
});
