#!/usr/local/bin/python3
import unittest
import random
import inspect
from InsertionSort import InsertionSort

class TestInsertionSort(unittest.TestCase):
    def setUp(self):
        self.insertionSort = InsertionSort()

    def test_0(self):
        print("{} Can create InsertionSort object".format(inspect.stack()[0][3]))
        self.assertTrue(type(self.insertionSort) is InsertionSort)

    def test_1(self):
        print("{} When 1 is given, getPositionForNewVal returns 0".format(inspect.stack()[0][3]))
        self.assertEqual(0, self.insertionSort.getPositionForNewVal(0, []))

    def test_2(self):
        print("{} When 3 is given to [2,7,4], getPositionForNewVal returns 1".format(inspect.stack()[0][3]))
        self.assertEqual(1, self.insertionSort.getPositionForNewVal(3, [2,7,4]))

    def test_3(self):
        print("{} When 9 is given to [2,4,7], getPositionForNewVal returns 3".format(inspect.stack()[0][3]))
        self.assertEqual(3, self.insertionSort.getPositionForNewVal(9, [2,4,7]))

    def test_4(self):
        testList = [2,4,6,3,5]
        print("{} Slice index 0 from [2,4,6,3,5], should return [4,6,3,5]".format(testList).format(inspect.stack()[0][3]))
        self.assertEqual([4,6,3,5], self.insertionSort.slice(testList,0,1))

    def test_5(self):
        testList = [2,4,6,3,5]
        print("{} Slice index 5 from [2,4,6,3,5], should return [2,4,6,3,5]".format(testList).format(inspect.stack()[0][3]))
        self.assertEqual([2,4,6,3,5], self.insertionSort.slice(testList,5,1))

    def test_6(self):
        testList = [2,4,6,3,5]
        print("{} Remove index 2 from {}, should return [2,4,3,5]".format(inspect.stack()[0][3],testList))
        self.assertEqual([2,4,3,5], self.insertionSort.slice(testList,2,1))

    def test_7(self):
        testList = [2,4,6,3,5]
        print("{} Insert 2 at index 0 into {}, should return [2,2,4,6,3,5]".format(inspect.stack()[0][3],testList))
        self.assertEqual([2,2,4,6,3,5], self.insertionSort.insertAt(2,0,testList))

    def test_8(self):
        testList = [2,4,6,3,5]
        print("{} Insert 2 at last index into {}, should return [2,4,6,3,5,2]".format(inspect.stack()[0][3],testList))
        self.assertEqual([2,4,6,3,5,2], self.insertionSort.insertAt(2,len(testList),testList))

    def test_9(self):
        testList = [2,4,6,3,5]
        print("{} Insert 2 at index 2 into {}, should return [2,4,2,6,3,5]".format(inspect.stack()[0][3],testList))
        self.assertEqual([2,4,2,6,3,5], self.insertionSort.insertAt(2,2,testList))

    def test_10(self):
        print("{} When [3,2,5,4,7,4] is given, sort returns [2,3,4,4,5,7]".format(inspect.stack()[0][3]))
        self.assertEqual([2,3,4,4,5,7],self.insertionSort.sort([3,2,5,4,7,4]))

    def test_11(self):
        print("{} When [8682,2602,5961,4659,432,8230,111,3921,2841,5913,4876,800,6748,5720,4660,327,2305,3571,9919,8277,6168,2305,3359,9292,7043] is given, sort returns [111,327,432,800,2305,2305,2602,2841,3359,3571,3921,4659,4660,4876,5720,5913,5961,6168,6748,7043,8230,8277,8682,9292,9919]".format(inspect.stack()[0][3]))
        self.assertEqual([111,327,432,800,2305,2305,2602,2841,3359,3571,3921,4659,4660,4876,5720,5913,5961,6168,6748,7043,8230,8277,8682,9292,9919],self.insertionSort.sort([8682,2602,5961,4659,432,8230,111,3921,2841,5913,4876,800,6748,5720,4660,327,2305,3571,9919,8277,6168,2305,3359,9292,7043]))

    def test_12(self):
        hugeNumber = 5000
        print("{} Can sort HUGE list of {}".format(inspect.stack()[0][3],hugeNumber))
        hugeList = self.generateHugeList(hugeNumber)
        sortedHugeList = self.insertionSort.sort(hugeList)
        for i,num in enumerate(sortedHugeList[:-1]):
            self.assertGreater(sortedHugeList[i+1], sortedHugeList[i])

    def generateHugeList(self,length):
        return random.sample(range(length*10), length)

if __name__ == '__main__':
    unittest.main()
