#!/usr/local/bin/python3
import unittest
from Stack import Stack

class TestStack(unittest.TestCase):

    def test_init(self):
        print("Can create Stack object")
        stack = Stack()
        self.assertTrue(type(stack) is Stack)

    def test_newClass_isEmpty(self):
        print("Newly created stacks should be empty")
        stack = Stack()
        self.assertTrue(stack.isEmpty())

    def test_afterOnePush_sizeIsOne(self):
        print("After one push, stack size should be one")
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.getSize(), 1)

    def test_afterOnePushOnePop_sizeIsEmpty(self):
        print("After one push and one pop, should be empty")
        stack = Stack()
        stack.push(1)
        stack.pop()
        self.assertTrue(stack.isEmpty())

    def test_whenPoppedPassedLimit_stackUnderflows(self):
        print("When popped passed limit, stack underflows")
        stack = Stack()
        with self.assertRaises(Stack.Underflow):
            stack.pop()

    def test_whenTwoValuesArePushedAndOneIsPopped_sizeIsTwo(self):
        print("When two values are pushed then one is popped, size is one")
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.pop()
        self.assertEqual(stack.getSize(), 1)

    def test_whenOneIsPushed_OneIsPopped(self):
        print("When one is pushed one is popped")
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.pop(), 1)

    def test_whenOneAndTwoArePushed_TwoAndOneArePopped(self):
        print("When one and two are pushed two and one are popped")
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

    def test_whenOneisPushed_OneIsOnTop(self):
        print("When one is pushed, one is on top")
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.top(), 1)

    def test_whenStackIsEmpty_topThrowsEmpty(self):
        print("When stack is empty, top throws empty")
        stack = Stack()
        with self.assertRaises(Stack.Empty):
            stack.top()

    def test_givenStackWIthOneTwoPushed_findOneAndTwo(self):
        print("Given stack with one two pushed, find one and two")
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.find(1),1)
        self.assertEqual(stack.find(2),0)

    def test_givenStackWithoutTwo_findTwoReturnsNull(self):
        print("Given a stack with no two, find two returns none")
        stack = Stack()
        self.assertEqual(stack.find(2), None)

if __name__ == '__main__':
        unittest.main()
