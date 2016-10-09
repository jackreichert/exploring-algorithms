# Stack

- [Wikipedia](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
- [Stack kata, Jack's notes](https://www.jackreichert.com/2016/07/code-katas-stack/)

## Tests

0. Can create Stack object
1. Newly created stacks should be empty
2. After one push, stack size should be one
3. After one push and one pop, should be empty
4. When pushed passed limit, stack overflows
5. When popped passed limit, stack underflows
6. When two values are pushed then one is popped, size is one
7. When 1 is pushed 1 is popped
8. When 1 and 2 are pushed 2 and 1 are popped
9. When creating stack with negative size, should throw IllegalCapacity
10. When Creating stack with zero capacity, any push should overflow
11. When one is pushed, one is on top
12. When stack is empty, top throws empty
13. With zero capacity stack, top throws empty
14. Given stack with one two pushed, find one and two
15. Given a stack with no two, find two returns null

[Inspired by CleanCoders.com Eps. 4 extras](https://cleancoders.com/videos#clean-code-episode-4.
