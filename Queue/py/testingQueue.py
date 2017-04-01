#!/usr/local/bin/python3
import unittest
import inspect
from Queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_0(self):
        print("{} Can create Queue object".format(inspect.stack()[0][3]))
        self.assertTrue(type(self.queue) is Queue)

    def test_1(self):
        print("{} Newly created queues should be empty".format(inspect.stack()[0][3]))
        self.assertTrue(self.queue.isEmpty())

    def test_2(self):
        print("{} After one enqueue, queue size should be one".format(inspect.stack()[0][3]))
        self.queue.enqueue(1)
        self.assertEqual(self.queue.getSize(), 1)

    def test_3(self):
        print("{} After one enqueue and one dequeue, should be empty".format(inspect.stack()[0][3]))
        self.queue.enqueue(1)
        self.queue.dequeue()
        self.assertEqual(self.queue.getSize(),0)

    def test_4(self):
        print("(S) {} When enqueued passed limit, queue overflows".format(inspect.stack()[0][3]))

    def test_5(self):
        print("{} When dequeued passed limit, queue underflows".format(inspect.stack()[0][3]))
        with self.assertRaises(Queue.Underflow):
            self.queue.dequeue()

    def test_6(self):
        print("{} When two values are enqueued then one is dequeued, size is one".format(inspect.stack()[0][3]))
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.dequeue()
        self.assertEqual(self.queue.getSize(),1)

    def test_7(self):
        print("{} When 1 is enqueued 1 is dequeued".format(inspect.stack()[0][3]))
        self.queue.enqueue(1)
        self.assertEqual(self.queue.dequeue(),1)

    def test_8(self):
        print("{} When 1 and 2 are enqueued 1 and 2 are dequeued".format(inspect.stack()[0][3]))
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(),1)
        self.assertEqual(self.queue.dequeue(),2)

    def test_9(self):
        print("(S) {} When creating queue with negative size, should throw IllegalCapacity".format(inspect.stack()[0][3]))

    def test_10(self):
        print("(S) {} When Creating queue with zero capacity, any enqueue should overflow".format(inspect.stack()[0][3]))

    def test_11(self):
        print("{} When 1 is enqueued, 1 is on top".format(inspect.stack()[0][3]))
        self.queue.enqueue(1)
        self.assertEqual(self.queue.top(),1)

    def test_12(self):
        print("{} When queue is empty, top throws empty".format(inspect.stack()[0][3]))
        with self.assertRaises(Queue.Empty):
            self.queue.top()

    def test_13(self):
        print("(S) {} With zero capacity queue, top throws empty".format(inspect.stack()[0][3]))

    def test_14(self):
        print("{} Given queue with 1 2 enqueued, find 1 and 2".format(inspect.stack()[0][3]))
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.find(1),0)
        self.assertEqual(self.queue.find(2),1)

    def test_15(self):
        print("{} Given a queue with no 2, find(2) returns null".format(inspect.stack()[0][3]))
        self.assertEqual(self.queue.find(2),None)


if __name__ == '__main__':
    unittest.main()
