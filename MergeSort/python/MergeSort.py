#!/usr/local/bin/python3

class MergeSort:
    def sort(self,alist):
        if len(alist) > 1:
            mid = len(alist)//2
            leftHalf = alist[:mid]
            rightHalf = alist[mid:]

            self.sort(leftHalf)
            self.sort(rightHalf)

            self.merge(alist, leftHalf,rightHalf)

        return alist

    def merge(self,alist,leftHalf,rightHalf):
        i = 0
        j = 0
        k = 0
        self.result = leftHalf + rightHalf

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                alist[k] = leftHalf[i]
                i = i + 1
            else:
                alist[k] = rightHalf[j]
                j = j + 1
            k = k + 1

        while i < len(leftHalf):
            alist[k] = leftHalf[i]
            i = i + 1
            k = k + 1

        while j < len(rightHalf):
            alist[k] = rightHalf[j]
            j = j + 1
            k = k + 1
