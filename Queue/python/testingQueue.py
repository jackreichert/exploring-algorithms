#!/usr/local/bin/python3
import unittest
from Queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_1(self):
        print("1. Can create Queue object")
        self.assertTrue(type(self.queue) is Queue)

if __name__ == '__main__':
    unittest.main()
