#!/usr/local/bin/python3

class Queue:
    def __init__(self):
        self.size = 0
        self.values = []

    def isEmpty(self):
        return True

    def enqueue(self,value):
        self.size += 1
        self.values.append(value)

    def dequeue(self):
        if 0 == self.getSize():
            raise self.Underflow("Underflow")
        self.size -= 1
        return self.values.pop(0)

    def getSize(self):
        return self.size

    def top(self):
        if 0 == len(self.values):
            raise self.Empty("Empty")
        return self.values[0]

    def find(self, value):
        try:
            return self.values.index(value)
        except Exception as e:
            return None

    class Underflow(Exception):
	       pass

    class Empty(Exception):
	       pass
