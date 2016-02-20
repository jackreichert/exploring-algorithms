#!/usr/local/bin/python3
'''
# Write a method that replaces all spaces with %20
'''
def replaceSpace_0(str):
  # well, this is the obvious option
  # cost: n
  return str.strip().replace(" ", "%20")

def replaceSpace_1(str):
  # loop through char by char, if char == " " replace it
  # cost: n
  str1,last_char = "",0
  for i,c in enumerate(str):
    if " " != c:
      last_char = i
      str1 += c
    else:
      str1 += "%20"
  print(i)
  return str1

def main():
  str = "Hello World!   "
  print(replaceSpace_0(str))
  print(replaceSpace_1(str))

if __name__ == "__main__": main()
