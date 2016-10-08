#!/usr/local/bin/python3

class SelectionSort:
    def __init__(self):
        pass

    def findLowest(self,numberList):
        lowest = 0
        for i,num in enumerate(numberList):
            if num < numberList[lowest]:
                lowest = i
        return lowest

    def swap(self,numberList,fromPos,toPos):
        tmpNum = numberList[fromPos]
        numberList[fromPos] = numberList[toPos]
        numberList[toPos] = tmpNum
        return numberList

    def sort(self,numberList):
        for i,x in enumerate(numberList):
            numberList = self.swap(numberList,i,i+self.findLowest(numberList[i:]))
        return numberList
