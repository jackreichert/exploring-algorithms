#!/usr/local/bin/python3
'''
linear search
'''

def linearSearch(A,val):
    for i in range(0, len(A)):
        if val == A[i]:
            return i
    return False

def linearSearchRecurse(A, val):
    length = len(A)
    if length == 0:
        return False
    elif(val == A[length-1]):
        return length-1
    else:
        return linearSearchRecurse(A[:length-2], val)


def main():
    arr = [5,2,4,6,1,3]
    print(linearSearch(arr, 6))
    print(linearSearchRecurse(arr, 6))

if __name__ == "__main__": main()
