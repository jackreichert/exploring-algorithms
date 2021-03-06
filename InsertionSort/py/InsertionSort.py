#!/usr/local/bin/python3

class InsertionSort:
    def __init__(self):
        pass

    def getPositionForNewVal(self, val, list):
        for i,num in enumerate(list):
            if val < num:
                return i
        return len(list)

    def slice(self,list,index,length):
        return list[:index] + list[index+length:]

    def insertAt(self,val, index, list):
        return list[:index] + [val] + list[index:]

    def sort(self, list):
        for i,num in enumerate(list):
            if i < len(list):
                newPos = self.getPositionForNewVal(num,list[:i])
                list = self.slice(list,i,1)
                list = self.insertAt(num,newPos,list)
        return list
