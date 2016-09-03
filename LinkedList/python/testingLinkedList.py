#!/usr/local/bin/python3
import unittest
from LinkedList import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linkedList = LinkedList()

    def test_1(self):
        print("1. Can create linked list object")
        self.assertTrue(type(self.linkedList) is LinkedList)

    def test_2(self):
        print("2. Newly created linked list, value and next should be null")
        last = self.linkedList.getNext()
        self.assertEqual(last.value, None)
        self.assertEqual(last.next, None)

    def test_3(self):
        print("3. Newly created list, should be empty")
        self.assertTrue(self.linkedList.isEmpty())

    def test_4(self):
        print("4. After one added, list size should be one")
        self.linkedList.add(1)
        self.assertEqual(self.linkedList.getSize(), 1)

    def test_5(self):
        print("5. After two added, list size should be two")
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.assertEqual(self.linkedList.getSize(), 2)

    def test_6(self):
        print("6. After one added, first index search should return value")
        self.linkedList.add(1)
        self.assertEqual(self.linkedList.searchValueAt(0),1)

    def test_7(self):
        print("7. After one added, second index search should return null")
        self.linkedList.add(1)
        self.assertEqual(self.linkedList.searchValueAt(1),None)

    def test_8(self):
        print("8. When two values are added, second index search should return second value")
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.assertEqual(self.linkedList.searchValueAt(1),2)

    def test_9(self):
        print("9. When two values are added, first index search should return first value")
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.assertEqual(self.linkedList.searchValueAt(0),1)

    def test_10(self):
        print("10. Remove first node on empty list, should return null")
        self.assertEqual(self.linkedList.removeAtInd(0), None)

    def test_11(self):
        print("11. After one added then remove first node, list should be empty")
        self.linkedList.add(1)
        self.linkedList.removeAtInd(0)
        self.assertTrue(self.linkedList.isEmpty())

    def test_12(self):
        print("12. After one added then remove first node, then add another value, first index should have second value")
        self.linkedList.add(1)
        self.linkedList.removeAtInd(0)
        self.linkedList.add(2)
        self.assertEqual(self.linkedList.searchValueAt(0),2)

    def test_13(self):
        print("13. After two values added then second value removed, length of list should be one")
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.linkedList.removeAtInd(1)
        self.assertEqual(self.linkedList.getSize(),1)

    def test_14(self):
        print("14. After two values added then value at third index removed, length of list should be two")
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.linkedList.removeAtInd(2)
        self.assertEqual(self.linkedList.getSize(),2)

    def test_15(self):
        print("15. After two values added then second value removed, first index should be first value and value of second index should be null")
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.linkedList.removeAtInd(1)
        self.assertEqual(self.linkedList.searchValueAt(1),None)
        self.assertEqual(self.linkedList.searchValueAt(1),None)

    def test_16(self):
        print("16. After two added then remove first node, length should be one")
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.linkedList.removeAtInd(0)
        self.assertEqual(self.linkedList.getSize(),1)

    def test_17(self):
        print("17. After two values added then remove first, value at first index should be second value pushed")
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.linkedList.removeAtInd(0)
        self.assertEqual(self.linkedList.searchValueAt(1),2)

    def test_18(self):
        print("18. After three values added then remove second, length should be two")
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.linkedList.add(3)
        self.linkedList.removeAtInd(1)
        self.assertEqual(self.linkedList.getSize(),2)

    def test_19(self):
        print("19. After three values added then remove second,  at first index should be first value and value at second index should be third value")
        self.linkedList.add(1)
        self.linkedList.add(2)
        self.linkedList.add(3)
        self.linkedList.removeAtInd(1)
        self.assertEqual(self.linkedList.searchValueAt(0),1)
        self.assertEqual(self.linkedList.searchValueAt(1),3)

if __name__ == '__main__':
    unittest.main()
