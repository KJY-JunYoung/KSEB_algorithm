
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, data):
        self._size = self._size + 1
        node = Node(data)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node     # increase rear

    def dequeue(self):
        if self.front is None:
            raise IndexError('dequeue from empty queue')
        self._size = self._size - 1
        temp = self.front # back up
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data

    def size(self):
        return self._size

if __name__ == "__main__":
    q = Queue()
    q.enqueue(7)
    q.enqueue(-11)
    q.enqueue(8)
    print(q.size())
    print(q.dequeue())
    print(q.size())