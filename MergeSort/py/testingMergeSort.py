#!/usr/local/bin/python3
import unittest
import random
import inspect
from MergeSort import MergeSort

class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.mergeSort = MergeSort()

    def test_0(self):
        print("{} Can create MergeSort object".format(inspect.stack()[0][3]))
        self.assertTrue(type(self.mergeSort) is MergeSort)

    def test_1(self):
        listToSort = [1]
        expectedResult = [1]
        print("{} When {} is given, sort returns {}".format(inspect.stack()[0][3],listToSort, expectedResult))
        self.assertEqual(expectedResult,self.mergeSort.sort(listToSort))

    def test_2(self):
        listToSort = [2,1]
        expectedResult = [1,2]
        print("{} When {} is given, sort returns {}".format(inspect.stack()[0][3],listToSort, expectedResult))
        self.assertEqual(expectedResult,self.mergeSort.sort(listToSort))

    def test_3(self):
        listToSort = [3,2,1]
        expectedResult = [1,2,3]
        print("{} When {} is given, sort returns {}".format(inspect.stack()[0][3],listToSort, expectedResult))
        self.assertEqual(expectedResult,self.mergeSort.sort(listToSort))

    def test_4(self):
        listToSort = [2,3,1]
        expectedResult = [1,2,3]
        print("{} When {} is given, sort returns {}".format(inspect.stack()[0][3],listToSort, expectedResult))
        self.assertEqual(expectedResult,self.mergeSort.sort(listToSort))

    def test_5(self):
        listToSort = [1,3,2]
        expectedResult = [1,2,3]
        print("{} When {} is given, sort returns {}".format(inspect.stack()[0][3],listToSort, expectedResult))
        self.assertEqual(expectedResult,self.mergeSort.sort(listToSort))

    def test_6(self):
        listToSort = [3,2,2,1]
        expectedResult = [1,2,2,3]
        print("{} When {} is given, sort returns {}".format(inspect.stack()[0][3],listToSort, expectedResult))
        self.assertEqual(expectedResult,self.mergeSort.sort(listToSort))

    def test_7(self):
        hugeNumber = 50000
        print("{} Can sort HUGE list of {}".format(inspect.stack()[0][3],hugeNumber))
        hugeList = self.generateHugeList(hugeNumber)
        sortedHugeList = self.mergeSort.sort(hugeList)
        for i,num in enumerate(sortedHugeList[:-1]):
            self.assertGreater(sortedHugeList[i+1], sortedHugeList[i])

    def generateHugeList(self,length):
        return random.sample(range(length*10), length)

if __name__ == '__main__':
    unittest.main()
