'''
linear search
'''

def linearSearch(val,A):
    for i in range(0, len(A)):
        if val == A[i]:
            return i
    return False

def main():
    pass

if __name__ == "__main__": main()
