#!/usr/local/bin/python3
'''
Selection sort: find lowest value, put in A[0] etc.
'''
def selectionSort(A):
    j = 0
    while j < len(A):
        lowest = A[j]
        lowestInd = j
        for i in range(j, len(A)):
            if A[i] < lowest:
                lowest = A[i]
                lowestInd = i
        A[lowestInd] = A[j]
        A[j] = lowest
        j += 1
    return A

def main():
    arr = [5,2,4,6,1,3]
    print("Before: {}".format(arr))
    print("After:  {}".format(selectionSort(arr)))

if __name__ == "__main__": main()
