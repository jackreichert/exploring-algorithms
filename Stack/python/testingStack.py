#!/usr/local/bin/python3
import unittest
from Stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_1(self):
        print("1. Can create Stack object")
        self.assertTrue(type(self.stack) is Stack)

    def test_2(self):
        print("2. Newly created stacks should be empty")
        self.assertTrue(self.stack.isEmpty())

    def test_3(self):
        print("3. After one push, stack size should be one")
        self.stack.push(1)
        self.assertEqual(self.stack.getSize(), 1)

    def test_4(self):
        print("4. After one push and one pop, should be empty")
        self.stack.push(1)
        self.stack.pop()
        self.assertTrue(self.stack.isEmpty())

    def test_6(self):
        print("6. When popped passed limit, stack underflows")
        with self.assertRaises(Stack.Underflow):
            self.stack.pop()

    def test_7(self):
        print("7. When two values are pushed then one is popped, size is one")
        self.stack.push(1)
        self.stack.push(2)
        self.stack.pop()
        self.assertEqual(self.stack.getSize(), 1)

    def test_8(self):
        print("8. When 1 is pushed 1 is popped")
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)

    def test_9(self):
        print("9. When 1 and 2 are pushed 2 and 1 are popped")
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_12(self):
        print("12. When one is pushed, one is on top")
        self.stack.push(1)
        self.assertEqual(self.stack.top(), 1)

    def test_13(self):
        print("13. When stack is empty, top throws empty")
        with self.assertRaises(Stack.Empty):
            self.stack.top()

    def test_15(self):
        print("15. Given stack with one two pushed, find one and two")
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.find(1),1)
        self.assertEqual(self.stack.find(2),0)

    def test_16(self):
        print("16. Given a stack with no two, find two returns null")
        self.assertEqual(self.stack.find(2), None)

if __name__ == '__main__':
        unittest.main()
