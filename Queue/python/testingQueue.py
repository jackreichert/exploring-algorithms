#!/usr/local/bin/python3
import unittest
from Queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_1(self):
        print("1. Can create Queue object")
        self.assertTrue(type(self.queue) is Queue)

    def test_2(self):
        print("2. Newly created queues should be empty")
        self.assertTrue(self.queue.isEmpty())

    def test_3(self):
        print("3. After one enqueue, queue size should be one")
        self.queue.enqueue(1)
        self.assertEqual(self.queue.getSize(), 1)

    def test_4(self):
        print("4. After one enqueue and one dequeue, should be empty")
        self.queue.enqueue(1)
        self.queue.dequeue()
        self.assertEqual(self.queue.getSize(),0)

    def test_5(self):
        print("(S) 5. When enqueued passed limit, queue overflows")

    def test_6(self):
        print("6. When dequeued passed limit, queue underflows")
        with self.assertRaises(Queue.Underflow):
            self.queue.dequeue()

    def test_7(self):
        print("7. When two values are enqueued then one is dequeued, size is one")
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.dequeue()
        self.assertEqual(self.queue.getSize(),1)

    def test_8(self):
        print("8. When 1 is enqueued 1 is dequeued")
        self.queue.enqueue(1)
        self.assertEqual(self.queue.dequeue(),1)

    def test_9(self):
        print("9. When 1 and 2 are enqueued 1 and 2 are dequeued")
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(),1)
        self.assertEqual(self.queue.dequeue(),2)

    def test_12(self):
        print("12. When 1 is enqueued, 1 is on top")
        self.queue.enqueue(1)
        self.assertEqual(self.queue.top(),1)

    def test_13(self):
        print("13. When queue is empty, top throws empty")
        with self.assertRaises(Queue.Empty):
            self.queue.top()

    def test_15(self):
        print("15. Given queue with 1 2 enqueued, find 1 and 2")
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.find(1),0)
        self.assertEqual(self.queue.find(2),1)

    def test_16(self):
        print("16. Given a queue with no 2, find(2) returns null")
        self.assertEqual(self.queue.find(2),None)


if __name__ == '__main__':
    unittest.main()
