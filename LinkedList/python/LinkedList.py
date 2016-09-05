#!/usr/local/bin/python3

class LinkedList:
    def __init__(self):
        self.head = self.Node()
        self.size = 0

    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

        def __str__(self):
            return str(self.value)

    def isEmpty(self):
        return 0 == self.size

    def add(self, value):
        lastNode = self.getNext()
        lastNode.value = value
        lastNode.next = self.Node()
        self.size = self.size + 1
        return self.size

    def getSize(self):
        return self.size

    def searchValueAt(self,ind):
        return self.searchNodeAt(ind).value

    def searchNodeAt(self,ind):
        currIndex = 0
        currNode = self.head
        while (currIndex < ind):
            currNode = currNode.next
            currIndex += 1
        return currNode

    def getNext(self):
        return self.searchNodeAt(self.size)

    def removeAtInd(self,ind):
        if ind == self.size:
            return

        beforeNode = self.searchNodeAt(ind-1)
        currNode = beforeNode.next
        if 0 == ind:
            currNode = self.head

        if None == currNode.next:
            currNode.next = self.Node()

        nextNode = currNode.next
        beforeNode.next = nextNode
        if (None != currNode.next or 0 == ind):
            self.size -= 1

        return currNode.value


    def __str__(self):
        str = ""
        currNode = self.head
        while (None != currNode.next):
            str = "{},{}".format(str,currNode)
            currNode = currNode.next
        return str[1:]
