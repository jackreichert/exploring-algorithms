#!/usr/local/bin/python3
import unittest
from Stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_init(self):
        print("Can create Stack object")
        self.assertTrue(type(self.stack) is Stack)

    def test_newClass_isEmpty(self):
        print("Newly created stacks should be empty")
        self.assertTrue(self.stack.isEmpty())

    def test_afterOnePush_sizeIsOne(self):
        print("After one push, stack size should be one")
        self.stack.push(1)
        self.assertEqual(self.stack.getSize(), 1)

    def test_afterOnePushOnePop_sizeIsEmpty(self):
        print("After one push and one pop, should be empty")
        self.stack.push(1)
        self.stack.pop()
        self.assertTrue(self.stack.isEmpty())

    def test_whenPoppedPassedLimit_stackUnderflows(self):
        print("When popped passed limit, stack underflows")
        with self.assertRaises(Stack.Underflow):
            self.stack.pop()

    def test_whenTwoValuesArePushedAndOneIsPopped_sizeIsTwo(self):
        print("When two values are pushed then one is popped, size is one")
        self.stack.push(1)
        self.stack.push(2)
        self.stack.pop()
        self.assertEqual(self.stack.getSize(), 1)

    def test_whenOneIsPushed_OneIsPopped(self):
        print("When one is pushed one is popped")
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)

    def test_whenOneAndTwoArePushed_TwoAndOneArePopped(self):
        print("When one and two are pushed two and one are popped")
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_whenOneisPushed_OneIsOnTop(self):
        print("When one is pushed, one is on top")
        self.stack.push(1)
        self.assertEqual(self.stack.top(), 1)

    def test_whenStackIsEmpty_topThrowsEmpty(self):
        print("When stack is empty, top throws empty")
        with self.assertRaises(Stack.Empty):
            self.stack.top()

    def test_givenStackWIthOneTwoPushed_findOneAndTwo(self):
        print("Given stack with one two pushed, find one and two")
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.find(1),1)
        self.assertEqual(self.stack.find(2),0)

    def test_givenStackWithoutTwo_findTwoReturnsNull(self):
        print("Given a stack with no two, find two returns none")
        self.assertEqual(self.stack.find(2), None)

if __name__ == '__main__':
        unittest.main()
