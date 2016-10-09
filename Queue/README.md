# Queue

- [Wikipedia](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))

## Tests

0. Can create Queue object
1. Newly created queues should be empty
2. After one enqueue, queue size should be one
3. After one enqueue and one dequeue, should be empty
4. When enqueued passed limit, queue overflows
5. When dequeued passed limit, queue underflows
6. When two values are enqueued then one is dequeued, size is one
7. When 1 is enqueued 1 is dequeued
8. When 1 and 2 are enqueued 1 and 2 are dequeued
9. When creating queue with negative size, should throw IllegalCapacity
10. When Creating queue with zero capacity, any enqueue should overflow
11. When 1 is enqueued, 1 is on top
12. When queue is empty, top throws empty
13. With zero capacity queue, top throws empty
14. Given queue with 1 2 enqueued, find 1 and 2
15. Given a queue with no 2, find(2) returns null
