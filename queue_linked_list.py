from linked_list import _Node, LinkedList
from typing import List, Any, Optional

class Queue:
    """
    This is a queue implemented using linked list
    """
    def __init__(self):
        self.item = LinkedList([])

    def is_empty(self) -> bool:
        """
        Return whether this queue contains no items
        """
        return self.item.is_empty()

    def enqueue(self, item: Any):
        """Add <item> to the back of this queue.
        """
        tmp = None
        if not self.is_empty():
            tmp = self.item._first
        self.item._first = _Node(item)
        if tmp is not None:
            self.item._first.next = tmp

    def dequeue(self) -> Optional[Any]:
        """Remove and return the item at the front of this queue.

        Return None if this Queue is empty.
        (We illustrate a different mechanism for handling an erroneous case.)

        >>> q = Queue()
        >>> q.enqueue('hello')
        >>> q.enqueue('goodbye')
        >>> q.dequeue()
        'hello'
        """
        curr = self.item._first
        while curr.next is not None:
            curr = curr.next
        tmp = curr.item
        curr.item = None
        return tmp


if __name__ == '__main__':
    import doctest
    doctest.testmod()
