class Empty(Exception):
    pass


class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """O(1)"""
        return self._size

    def is_empty(self):
        """O(1)"""
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None  # removed head had been the tail
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        if len(self) > 1:
            new_head = self._head._next
            self._head._next = None
            self._tail._next = self._head
            self._tail = self._head
            self._head = new_head

    def __str__(self):
        str_lst = []
        cur = self._head
        while cur:
            str_lst.append(str(cur._element))
            cur = cur._next
        return ', '.join(str_lst)


if __name__ == "__main__":
    lg = LinkedQueue()
    print(lg.is_empty())
    try:
        lg.dequeue()
    except Exception as e:
        print(e)
    lg.enqueue(2)
    print(lg.is_empty())
    lg.enqueue(5)
    print(lg.dequeue())
    print(lg.dequeue())
    print(lg.is_empty())
    lg.enqueue(2)
    lg.enqueue(3)
    lg.enqueue(5)
    print(lg)
    lg.rotate()
    print(lg)
    lg.rotate()
    print(lg)

