class myQueue:

    def __init__(self):
        # Initialize your data members
        self.q = []

    def enqueue(self, x):
        # Implement the enqueue operation
        self.q.append(x)

    def dequeue(self):
        # Implement the dequeue operation
        if self.size() == 0:
            return -1  # Standard to return -1 or raise error if empty
        return self.q.pop(0)

    def front(self):
        # Return the front element of the queue
        if self.size() == 0:
            return -1
        return self.q[0]

    def size(self):
        # Return the current size of the queue
        return len(self.q)
