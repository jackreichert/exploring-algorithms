'use strict';
QUnit.test( "Can create Stack object", function( assert ) {
  var stack = new Stack();
  assert.ok( 'Stack' === stack.constructor.name, "Passed!" );
});

QUnit.test( "Newly created stacks should be empty", function ( assert ) {
  var stack = new Stack();
  assert.ok( 0 === stack.getSize(), "Passed!");
  assert.ok( stack.isEmpty(), "Passed!" );
});

QUnit.test( "After one push, stack size should be one", function ( assert ) {
  var stack = new Stack();
  stack.push(1);
  assert.ok( 1 === stack.getSize(), "Passed!");
  assert.ok( !stack.isEmpty(), "Passed!" );
})

QUnit.test( "After one push and one pop, should be empty", function(assert) {
  var stack = new Stack();
  stack.push(1);
  stack.pop();
  assert.ok( stack.isEmpty(), "Passed!" );
});

// QUnit.test( "When pushed passed limit, stack overflows");

QUnit.test( "When popped passed limit, stack underflows", function (assert) {
  assert.throws(
    function() {
      var stack = new Stack();
      stack.push(1);
      stack.pop();
      stack.pop();
    }, new Error("StackUnderflow"), "Passed!" );
});

QUnit.test( "When two values are pushed then one is popped, size is one", function(assert) {
  var stack = new Stack();
  stack.push(1);
  stack.push(2);
  stack.pop();
  assert.ok( 1 === stack.getSize(), "Passed!" );
});

QUnit.test( "When one is pushed one is popped", function (assert) {
  var stack = new Stack();
  stack.push(1);
  assert.ok( 1 === stack.pop(), "Passed!" );
});

QUnit.test( "When one and two are pushed two and one are popped", function (assert) {
  var stack = new Stack();
  stack.push(1);
  stack.push(2);
  assert.ok( 2 === stack.pop(), "Passed!" );
  assert.ok( 1 === stack.pop(), "Passed!" );
});

// QUnit.test("When creating stack with negative size, should through IllegalCapacity");

// QUnit.test("When Creating stack with zero capacity, any push should overflow");

QUnit.test( "When one is pushed, one is on top", function (assert) {
  var stack = new Stack();
  stack.push(1);
  assert.ok( 1 === stack.top(), "Passed!");
  assert.ok( 1 === stack.getSize(), "Passed!");
});

QUnit.test("When stack is empty, top throws empty", function (assert) {
  assert.throws(function () {
    var stack = new Stack();
    stack.top();
  }, new Error("Empty"), 'Passed!');
});

// QUnit.test("With zero capacity stack, top throws empty");

QUnit.test("Given stack with one two pushed, find one and two", function (assert) {
    var stack = new Stack();
    stack.push(1);
    stack.push(2);
    assert.ok( 1 == stack.find(1), "Passed!" );
    assert.ok( 0 == stack.find(2), "Passed!" );
});

QUnit.test("Given a stack with no two, find two returns null", function (assert) {
  var stack = new Stack();
  assert.ok(null == stack.find(2), "Passed!");
});
