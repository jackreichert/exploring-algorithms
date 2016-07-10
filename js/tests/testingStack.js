QUnit.test( "new stack test", function( assert ) {
  var stack = new Stack();
  assert.ok( undefined !== stack, "Passed!" );
});

QUnit.test( "new stack is empty", function ( assert ) {
  var stack = new Stack();
  assert.ok( true === stack.isEmpty(), "Passed!" );
});

QUnit.test( "Push one, size is one", function ( assert ) {
  var stack = new Stack();
  stack.push(1);
  assert.ok( 1 === stack.getSize(), "Passed!");
})

QUnit.test( "Push two, then pop one, size is one", function(assert) {
  var stack = new Stack();
  stack.push(1);
  stack.push(2);
  stack.pop();
  assert.ok( 1 === stack.getSize(), "Passed!" );
});

QUnit.test( "Push one and pop two, throws exception stack underflow", function (assert) {
  assert.throws(
    function() {
      var stack = new Stack();
      stack.push(1);
      stack.pop();
      stack.pop();
    }, new Error("StackUnderflow"), "Passed!" );
});

QUnit.test( "Push number 5 then pop, result is 5", function (assert) {
  var stack = new Stack();
  stack.push(5);
  assert.ok( 5 === stack.pop(), "Passed!" );
});

QUnit.test( "Push number 5, peek returns 5, size remains", function (assert) {
  var stack = new Stack();
  stack.push(5);
  assert.ok( 5 === stack.peek(), "Passed!");
  assert.ok( 1 === stack.getSize(), "Passed!");
});
