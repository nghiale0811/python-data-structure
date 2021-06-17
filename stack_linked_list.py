from linked_list import _Node, LinkedList
from typing import List, Any, Optional


class EmptyStackError(Exception):
    """Exception raised when an error occurs."""
    pass


class Stack:
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

    def push(self, item: Any):
        """Add a new element to the top of this stack."""
        tmp = None
        if not self.is_empty():
            tmp = self.item._first
        self.item._first = _Node(item)
        if tmp is not None:
            self.item._first.next = tmp

    def pop(self) -> Optional[Any]:
        """Remove and return the element at the top of this stack.

        Raise an EmptyStackError if this stack is empty.

        >>> s = Stack()
        >>> s.push('hello')
        >>> s.push('goodbye')
        >>> s.pop()
        'goodbye'
        """
        if self.item.is_empty():
            raise EmptyStackError
        tmp = self.item._first.item
        self.item._first = self.item._first.next
        return tmp


if __name__ == '__main__':
    import doctest
    doctest.testmod()
