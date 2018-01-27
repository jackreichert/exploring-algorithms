#!/usr/local/bin/python3

class SelectionSort:
    def  __init__(self):
        pass

    def findIndexOfLowestInList(self, numberList):
        lowest = 0

        for i,num in enumerate(numberList):
            if num < numberList[lowest]:
                lowest = i
        return lowest

    def swapFromTo(self,numberList,fromPos,toPos):
        tempNum = numberList[fromPos]
        numberList[fromPos] = numberList[toPos]
        numberList[toPos] = tempNum
        return numberList

    def sort(self,numberList):
        for i,num in enumerate(numberList):
            numberList = self.swapFromTo(numberList, i, i+self.findIndexOfLowestInList(numberList[i:]))
        return numberList
