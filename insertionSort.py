#!/usr/local/bin/python3
'''
    Given an array, will sort it using Insertion sort
'''
def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        # if A[i] is out of place, move it to it's place
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A



def main():
    arr = [5,2,4,6,1,3]
    print("Before: {}".format(arr))
    print("After:  {}".format(insertionSort(arr)))

if __name__ == "__main__": main()
