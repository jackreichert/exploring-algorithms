#!/usr/local/bin/python3
import unittest
import random
import inspect
from SelectionSort import SelectionSort

class TestSelectionSort(unittest.TestCase):
    def setUp(self):
        self.selectionSort = SelectionSort()

    def test_0(self):
        print("{} Can create SelectionSort object".format(inspect.stack()[0][3]))
        self.assertTrue(type(self.selectionSort) is SelectionSort)

    def test_1(self):
        print("{} When given list of unique positive numbers, can find lowest number".format(inspect.stack()[0][3]))
        numberList = [3,2,5]
        self.assertEqual(numberList[self.selectionSort.findLowest(numberList)], 2)

    def test_2(self):
        print("{} When given list of unique numbers, can find lowest number".format(inspect.stack()[0][3]))
        numberList = [3,2,-5]
        self.assertEqual(numberList[self.selectionSort.findLowest(numberList)], -5)

    def test_3(self):
        print("{} When given list of numbers, can find lowest number".format(inspect.stack()[0][3]))
        numberList = [3,2,2,5]
        self.assertEqual(numberList[self.selectionSort.findLowest(numberList)], 2)

    def test_4(self):
        print("{} Swapping numbers in small list, where from > to".format(inspect.stack()[0][3]))
        numberList = [2,3,4]
        self.assertEqual(self.selectionSort.swap(numberList,2,0), [4,3,2])

    def test_5(self):
        print("{} Swapping numbers in small list, where from < to".format(inspect.stack()[0][3]))
        numberList = [2,3,4]
        self.assertEqual(self.selectionSort.swap(numberList,0,2), [4,3,2])

    def test_6(self):
        print("{} Can sort small list".format(inspect.stack()[0][3]))
        numberList = [2,3,5,6,4,7]
        self.assertEqual([2,3,4,5,6,7], self.selectionSort.sort(numberList))

    def test_7(self):
        print("{} Can sort HUGE list".format(inspect.stack()[0][3]))
        hugeList = self.generateHugeList(1000)
        sortedHugeList = self.selectionSort.sort(hugeList)
        for i,num in enumerate(sortedHugeList[:-1]):
            self.assertGreater(sortedHugeList[i+1], sortedHugeList[i])

    def generateHugeList(self,length):
        return random.sample(range(length*10), length)


if __name__ == '__main__':
    unittest.main()
