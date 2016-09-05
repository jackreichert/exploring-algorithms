# Queue

- [Wikipedia](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))

## Tests

1. Can create Queue object
2. Newly created queues should be empty
3. After one enqueue, queue size should be one
4. After one enqueue and one dequeue, should be empty
5. When enqueued passed limit, queue overflows
6. When dequeued passed limit, queue underflows
7. When two values are enqueued then one is dequeued, size is one
8. When 1 is enqueued 1 is dequeued
9. When 1 and 2 are enqueued 1 and 2 are dequeued
10. When creating queue with negative size, should throw IllegalCapacity
11. When Creating queue with zero capacity, any enqueue should overflow
12. When 1 is enqueued, 1 is on top
13. When queue is empty, top throws empty
14. With zero capacity queue, top throws empty
15. Given queue with 1 2 enqueued, find 1 and 2
16. Given a queue with no 2, find(2) returns null
