QUnit.test("New linked list init", function (assert) {
  var linkedList = new LinkedList();
  assert.ok(undefined !== linkedList, 'Passed!');
});

QUnit.test("New linked list, next is null", function (assert) {
  var linkedList = new LinkedList();
  assert.ok(null === linkedList.getNext(), 'Passed!');
});

QUnit.test("New Linked list, getLength is 0", function (assert) {
  var linkedList = new LinkedList();
  assert.ok(0 === linkedList.getLength(), 'Passed!');
});

QUnit.test("Add value once to list, getLength is 1", function (assert) {
  var linkedList = new LinkedList();
  linkedList.add(5);
  assert.ok(1 === linkedList.getLength(), 'Passed!');
});

QUnit.test("Add value once, searchValueAt(0) returns value", function (assert) {
  var linkedList = new LinkedList();
  linkedList.add(5);
  assert.ok(5 === linkedList.searchValueAt(0), 'Passed!');
});

QUnit.test("Add two values, getLength is 2", function (assert) {
  var linkedList = new LinkedList();
  linkedList.add(5);
  linkedList.add(8);
  assert.ok(2 === linkedList.getLength(), 'Passed!');
});

QUnit.test("Add two values, searchValueAt(1) returns second value", function (assert) {
  var linkedList = new LinkedList();
  linkedList.add(5);
  linkedList.add(8);
  assert.ok(8 === linkedList.searchValueAt(1), 'Passed!');
});

QUnit.test("Add two values, searchValueAt(0) returns first value", function (assert) {
  var linkedList = new LinkedList();
  linkedList.add(5);
  linkedList.add(8);
  assert.ok(5 === linkedList.searchValueAt(0), 'Passed!');
});

QUnit.test("Add value, remove node, length is 0", function (assert) {
  var linkedList = new LinkedList();
  linkedList.add(5);
  linkedList.removeNodeAt(0);
  assert.ok(0 === linkedList.getLength(), 'Passed!');
});

QUnit.test("Add value, remove node, list is empty", function (assert) {
  var linkedList = new LinkedList();
  linkedList.add(5);
  linkedList.removeNodeAt(0);
  assert.ok(null === linkedList.searchValueAt(0), 'Passed!');
});

QUnit.test("Add two values, remove second, length is 1", function (assert) {
  var linkedList = new LinkedList();
  linkedList.add(5);
  linkedList.add(8);
  linkedList.removeNodeAt(1);
  assert.ok(1 === linkedList.getLength(), 'Passed!');
});

QUnit.test("Add two values, remove second, first is value and next is empty", function (assert) {
  var linkedList = new LinkedList();
  linkedList.add(5);
  linkedList.add(8);
  linkedList.removeNodeAt(1);
  assert.ok(5 === linkedList.searchValueAt(0), 'Passed!');
  assert.ok(null === linkedList.getNext(), 'Passed!');
});

QUnit.test("Add two values, remove first, length is 1", function (assert) {
  var linkedList = new LinkedList();
  linkedList.add(5);
  linkedList.add(8);
  linkedList.removeNodeAt(0);
  assert.ok(1 === linkedList.getLength(), 'Passed!');
});

QUnit.test("Add two values, remove first, first is second value", function (assert) {
  var linkedList = new LinkedList();
  linkedList.add(5);
  linkedList.add(8);
  linkedList.removeNodeAt(0);
  assert.ok(8 === linkedList.searchValueAt(0), 'Passed!');
});

QUnit.test("Add three values, remove second, length is 2", function (assert) {
  var linkedList = new LinkedList();
  linkedList.add(5);
  linkedList.add(8);
  linkedList.add(7);
  linkedList.removeNodeAt(1);
  assert.ok(2 === linkedList.getLength(), 'Passed!');
});

QUnit.test("Add three values, remove second, first is value and second is third value", function (assert) {
  var linkedList = new LinkedList();
  linkedList.add(5);
  linkedList.add(8);
  linkedList.add(7);
  linkedList.removeNodeAt(1);
  assert.ok(5 === linkedList.searchValueAt(0), 'Passed!');
  assert.ok(7 === linkedList.searchValueAt(1), 'Passed!');
});
