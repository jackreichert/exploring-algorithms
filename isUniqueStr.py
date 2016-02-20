#!/usr/local/bin/python3
'''
# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
You can ask if we'e dealing with ASCII or Unicode, if it's ASCII you can return False for any string longer than 128
'''
def isUniqueChars_0(str):
    # initial attempt, just get it done. Not efficient, but works
    # O(n^2) where n is len(str)
    for i,c in enumerate(str):
        for ind,ch in enumerate(str):
            if i != ind and c == ch:
                return False
    return True

def isUniqueChars_1(str):
    # attempt 1, doesn't use extra variables
    # (2n) where n is len(str)
    sorted_str = ''.join(sorted(str))
    for i in range(0,len(sorted_str)-1):
        if sorted_str[i] == sorted_str[i+1]:
            return False

    return True

def isUniqueChars_2(str, alphanumeric=False):
    # uses extra variable, but is quick as it doesn't need to sort the input first
    # O(n) where n is len(str)
    ar, exists = {}, False
    for c in str:
        try:
            exists = ar[c] == True
        except:
            ar[c] = True
    return not exists

def main():
    str0, str1, str2 = 'hello world', 'absABD', '!@#$%^QWEqwe'
    print( "unique" if isUniqueChars_0(str0) else "not unique")
    print( "unique" if isUniqueChars_1(str1) else "not unique")
    print( "unique" if isUniqueChars_2(str2) else "not unique")

if __name__ == "__main__": main()
