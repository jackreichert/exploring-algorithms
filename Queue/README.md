# Queue

- [Wikipedia](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))

## Tests

1. Can create Queue object
2. Newly created queues should be empty
3. After one push, queue size should be one
4. After one push and one dequeue, should be empty
5. When pushed passed limit, queue overflows
6. When dequeued passed limit, queue underflows
7. When two values are pushed then one is dequeued, size is one
9. When one and two are pushed one and two are dequeued
10. When creating queue with negative size, should throw IllegalCapacity
11. When Creating queue with zero capacity, any push should overflow
12. When one is pushed, one is on top
13. When queue is empty, top throws empty
14. With zero capacity queue, top throws empty
15. Given queue with one two pushed, find one and two
16. Given a queue with no two, find two returns null
