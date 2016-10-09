#!/usr/local/bin/python3
import unittest
import inspect
from Stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_0(self):
        print("{} Can create Stack object".format(inspect.stack()[0][3]))
        self.assertTrue(type(self.stack) is Stack)

    def test_1(self):
        print("{} Newly created stacks should be empty".format(inspect.stack()[0][3]))
        self.assertTrue(self.stack.isEmpty())

    def test_2(self):
        print("{} After one push, stack size should be one".format(inspect.stack()[0][3]))
        self.stack.push(1)
        self.assertEqual(self.stack.getSize(), 1)

    def test_3(self):
        print("{} After one push and one pop, should be empty".format(inspect.stack()[0][3]))
        self.stack.push(1)
        self.stack.pop()
        self.assertTrue(self.stack.isEmpty())

    def test_4(self):
        print("(S) {}When pushed passed limit, stack overflows".format(inspect.stack()[0][3]))

    def test_5(self):
        print("{} When popped passed limit, stack underflows".format(inspect.stack()[0][3]))
        with self.assertRaises(Stack.Underflow):
            self.stack.pop()

    def test_6(self):
        print("{} When two values are pushed then one is popped, size is one".format(inspect.stack()[0][3]))
        self.stack.push(1)
        self.stack.push(2)
        self.stack.pop()
        self.assertEqual(self.stack.getSize(), 1)

    def test_7(self):
        print("{} When 1 is pushed 1 is popped".format(inspect.stack()[0][3]))
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)

    def test_8(self):
        print("{} When 1 and 2 are pushed 2 and 1 are popped".format(inspect.stack()[0][3]))
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_9(self):
        print("(S) {} When creating stack with negative size, should throw IllegalCapacity".format(inspect.stack()[0][3]))

    def test_10(self):
        print("(S) {} When Creating stack with zero capacity, any push should overflow".format(inspect.stack()[0][3]))

    def test_11(self):
        print("{} When one is pushed, one is on top".format(inspect.stack()[0][3]))
        self.stack.push(1)
        self.assertEqual(self.stack.top(), 1)

    def test_12(self):
        print("{} When stack is empty, top throws empty".format(inspect.stack()[0][3]))
        with self.assertRaises(Stack.Empty):
            self.stack.top()

    def test_13(self):
        print("(S) {} With zero capacity stack, top throws empty".format(inspect.stack()[0][3]))

    def test_14(self):
        print("{} Given stack with one two pushed, find one and two".format(inspect.stack()[0][3]))
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.find(1),1)
        self.assertEqual(self.stack.find(2),0)

    def test_15(self):
        print("{} Given a stack with no two, find two returns null".format(inspect.stack()[0][3]))
        self.assertEqual(self.stack.find(2), None)

if __name__ == '__main__':
        unittest.main()
