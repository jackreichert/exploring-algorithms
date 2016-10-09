#!/usr/local/bin/python3
import unittest
import inspect
from LinkedList import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linkedList = LinkedList()

    def test_0(self):
        print("{} Can create linked list object".format(inspect.stack()[0][3]))
        self.assertTrue(type(self.linkedList) is LinkedList)

    def test_1(self):
        print("{} Newly created linked list, value and next should be null".format(inspect.stack()[0][3]))
        last = self.linkedList.getNext()
        self.assertEqual(last.value, None)
        self.assertEqual(last.next, None)

    def test_2(self):
        print("{} Newly created list, should be empty".format(inspect.stack()[0][3]))
        self.assertTrue(self.linkedList.isEmpty())

    def test_3(self):
        print("{} After one added, list size should be one".format(inspect.stack()[0][3]))
        self.linkedList.add(1)
        self.assertEqual(self.linkedList.getSize(), 1)

    def test_4(self):
        print("{} After two added, list size should be two".format(inspect.stack()[0][3]))
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.assertEqual(self.linkedList.getSize(), 2)

    def test_5(self):
        print("{} After one added, first index search should return value".format(inspect.stack()[0][3]))
        self.linkedList.add(1)
        self.assertEqual(self.linkedList.searchValueAt(0),1)

    def test_6(self):
        print("{} After one added, second index search should return null".format(inspect.stack()[0][3]))
        self.linkedList.add(1)
        self.assertEqual(self.linkedList.searchValueAt(1),None)

    def test_7(self):
        print("{} When two values are added, second index search should return second value".format(inspect.stack()[0][3]))
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.assertEqual(self.linkedList.searchValueAt(1),2)

    def test_8(self):
        print("{} When two values are added, first index search should return first value".format(inspect.stack()[0][3]))
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.assertEqual(self.linkedList.searchValueAt(0),1)

    def test_9(self):
        print("{} Remove first node on empty list, should return null".format(inspect.stack()[0][3]))
        self.assertEqual(self.linkedList.removeAtInd(0), None)

    def test_10(self):
        print("{} After one added then remove first node, list should be empty".format(inspect.stack()[0][3]))
        self.linkedList.add(1)
        self.linkedList.removeAtInd(0)
        self.assertTrue(self.linkedList.isEmpty())

    def test_11(self):
        print("{} After one added then remove first node, then add another value, first index should have second value".format(inspect.stack()[0][3]))
        self.linkedList.add(1)
        self.linkedList.removeAtInd(0)
        self.linkedList.add(2)
        self.assertEqual(self.linkedList.searchValueAt(0),2)

    def test_12(self):
        print("{} After two values added then second value removed, length of list should be one".format(inspect.stack()[0][3]))
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.linkedList.removeAtInd(1)
        self.assertEqual(self.linkedList.getSize(),1)

    def test_13(self):
        print("{} After two values added then value at third index removed, length of list should be two".format(inspect.stack()[0][3]))
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.linkedList.removeAtInd(2)
        self.assertEqual(self.linkedList.getSize(),2)

    def test_14(self):
        print("{} After two values added then second value removed, first index should be first value and value of second index should be null".format(inspect.stack()[0][3]))
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.linkedList.removeAtInd(1)
        self.assertEqual(self.linkedList.searchValueAt(1),None)
        self.assertEqual(self.linkedList.searchValueAt(1),None)

    def test_15(self):
        print("{} After two added then remove first node, length should be one".format(inspect.stack()[0][3]))
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.linkedList.removeAtInd(0)
        self.assertEqual(self.linkedList.getSize(),1)

    def test_16(self):
        print("{} After two values added then remove first, value at first index should be second value pushed".format(inspect.stack()[0][3]))
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.linkedList.removeAtInd(0)
        self.assertEqual(self.linkedList.searchValueAt(1),2)

    def test_17(self):
        print("{} After three values added then remove second, length should be two".format(inspect.stack()[0][3]))
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.linkedList.add(3)
        self.linkedList.removeAtInd(1)
        self.assertEqual(self.linkedList.getSize(),2)

    def test_18(self):
        print("{} After three values added then remove second,  at first index should be first value and value at second index should be third value".format(inspect.stack()[0][3]))
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.linkedList.add(3)
        self.linkedList.removeAtInd(1)
        self.assertEqual(self.linkedList.searchValueAt(0),1)
        self.assertEqual(self.linkedList.searchValueAt(1),3)

if __name__ == '__main__':
    unittest.main()
