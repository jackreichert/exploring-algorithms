# Insertion Sort

- [Wikipedia](https://en.wikipedia.org/wiki/Insertion_sort)
- [Insertion sort Kata, Jack's thoughts](https://www.jackreichert.com/2016/08/coding-katas-insertion-sort/)

## Tests

1. Can create InsertionSort object
2. When 1 is given, getPositionForNewVal returns 0
3. When 2 is given to [3,4], getPositionForNewVal returns 0
4. When 3 is given to [2,7,4], getPositionForNewVal returns 1
5. When [3,2,5,4,7,4] is given, sort returns [2,3,4,4,5,7]
6. When [8682,2602,5961,4659,432,8230,111,3921,2841,5913,4876,800,6748,5720,4660,327,2305,3571,9919,8277,6168,2305,3359,9292,7043] is given, sort returns [111,327,432,800,2305,2305,2602,2841,3359,3571,3921,4659,4660,4876,5720,5913,5961,6168,6748,7043,8230,8277,8682,9292,9919]
