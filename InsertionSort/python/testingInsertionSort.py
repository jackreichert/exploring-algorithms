#!/usr/local/bin/python3
import unittest
from InsertionSort import InsertionSort

class TestInsertionSort(unittest.TestCase):
    def setUp(self):
        self.insertionSort = InsertionSort()

    def test_init(self):
        print("Can create self.insertionSort object")
        self.assertTrue(type(self.insertionSort) is InsertionSort)

    def test_oneGivenGetPosition(self):
        print("When 1 is given, getPositionForNewVal returns 0")
        self.assertEqual(0, self.insertionSort.getPositionForNewVal(0, []))

    def test_valueGivenToListofTwo(self):
        print("When 3 is given to [2,7,4], getPositionForNewVal returns 1")
        self.assertEqual(1, self.insertionSort.getPositionForNewVal(3, [2,7,4]))

    def test_valueGivenLargerThanOthers(self):
        print("When 9 is given to [2,4,7], getPositionForNewVal returns 3")
        self.assertEqual(3, self.insertionSort.getPositionForNewVal(9, [2,4,7]))

    def test_removeFromListAtBeginning(self):
        testList = [2,4,6,3,5]
        print("Slice index 0 from [2,4,6,3,5], should return [4,6,3,5]".format(testList))
        self.assertEqual([4,6,3,5], self.insertionSort.slice(testList,0,1))

    def test_removeFromListAfterIndex(self):
        testList = [2,4,6,3,5]
        print("Slice index 5 from [2,4,6,3,5], should return [2,4,6,3,5]".format(testList))
        self.assertEqual([2,4,6,3,5], self.insertionSort.slice(testList,5,1))

    def test_removeFromListAtIndex(self):
        testList = [2,4,6,3,5]
        print("Remove index 2 from {}, should return [2,4,3,5]".format(testList))
        self.assertEqual([2,4,3,5], self.insertionSort.slice(testList,2,1))

    def test_insertAtIndexZero(self):
        testList = [2,4,6,3,5]
        print("Insert 2 at index 0 into {}, should return [2,2,4,6,3,5]".format(testList))
        self.assertEqual([2,2,4,6,3,5], self.insertionSort.insertAt(2,0,testList))

    def test_insertAtIndexLast(self):
        testList = [2,4,6,3,5]
        print("Insert 2 at last index into {}, should return [2,4,6,3,5,2]".format(testList))
        self.assertEqual([2,4,6,3,5,2], self.insertionSort.insertAt(2,len(testList),testList))

    def test_insertAtMidIndex(self):
        testList = [2,4,6,3,5]
        print("Insert 2 at index 2 into {}, should return [2,4,2,6,3,5]".format(testList))
        self.assertEqual([2,4,2,6,3,5], self.insertionSort.insertAt(2,2,testList))

    def test_sortShortList(self):
        print("When [3,2,5,4,7,4] is given, sort returns [2,3,4,4,5,7]")
        self.assertEqual([2,3,4,4,5,7],self.insertionSort.sort([3,2,5,4,7,4]))

    def test_sortShortList(self):
        print("When [8682,2602,5961,4659,432,8230,111,3921,2841,5913,4876,800,6748,5720,4660,327,2305,3571,9919,8277,6168,2305,3359,9292,7043] is given, sort returns [111,327,432,800,2305,2305,2602,2841,3359,3571,3921,4659,4660,4876,5720,5913,5961,6168,6748,7043,8230,8277,8682,9292,9919]")
        self.assertEqual([111,327,432,800,2305,2305,2602,2841,3359,3571,3921,4659,4660,4876,5720,5913,5961,6168,6748,7043,8230,8277,8682,9292,9919],self.insertionSort.sort([8682,2602,5961,4659,432,8230,111,3921,2841,5913,4876,800,6748,5720,4660,327,2305,3571,9919,8277,6168,2305,3359,9292,7043]))

if __name__ == '__main__':
    unittest.main()
