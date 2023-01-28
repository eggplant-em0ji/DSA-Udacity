I implemented a min-heap priority queue by creating a list then accessing elements in the min-heap according to list index.
This encoding implementation has a time complexity of O(nlog(n)) since up to n elements (if they are all unique) needs to be added to the queue and for each n after removing from or adding
to the queue, in worst case scenario, the min-heap has swap values to maintain its min-heap qualities, which takes up to log(n) time each time.
The space complexity is also O(nlog(n)) because up to n unique inputs and log(n) internal nodes can be stored.
The decoding operation takes O(n) time since it essentially performs one operation per 1 or 0 in the encoded sequence.