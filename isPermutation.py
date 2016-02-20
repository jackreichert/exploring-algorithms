#!/usr/local/bin/python3
'''
# Given two strings, wroite a method to decide if one is a permutation of the other.
**Assumptions**
- ignore whitespace
O() calculated with https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
'''

def isPermutation_0(str1, str2):
    # case insensitive
    # clean whitespace, sort letters, compare
    # roughly 2nlogn + 6n
    return "".join(sorted(str1.lower())).strip() == "".join(sorted(str2.lower())).strip()

def isPermutation_1(str1,str2):
    # character type agnostic
    # roughly 2 + 2n

    # if different lengths can't be permutation
    if len(str1) != len(str2):
        return False

    # count occurances of each character in each string
    a1,a2 = {},{}
    for i,c in enumerate(str1):
        a1[c] = a1[c] + 1 if isinstance( c, int ) else 1
        a2[str2[i]] = a2[str2[i]] + 1 if isinstance( c, int ) else 1

    # compare strings
    return a1 == a2

def main():
    str1, str2 = 'asdfghjkl ', ' lkjhgfdsa'
    print( "permutation" if isPermutation_1(str1,str2) else "not permutation")

    str1, str2 = 'qwertyus ', ' lkjhgfdsa'
    print( "permutation" if isPermutation_1(str1,str2) else "not permutation")

if __name__ == "__main__": main()
