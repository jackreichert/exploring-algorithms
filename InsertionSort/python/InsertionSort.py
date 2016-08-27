#!/usr/local/bin/python3

class InsertionSort:
    def __init__(self):
        pass

    def getPositionForNewVal(self, val, list):
        for i,num in enumerate(list):
            if val < num:
                return i
        return len(list)

    def insertAt(self,val,index,list):
        return list[:index] + [val] + list[index:]

    def sort(self,list):
        newlist = []
        for i,num in enumerate(list):
            if i < (len(list)):
                newPos = self.getPositionForNewVal(num,newlist)
                newlist = self.insertAt(num,newPos,newlist)
        return newlist
